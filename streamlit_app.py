import streamlit as st
import pandas as pd
import requests
import time
import os
from datetime import datetime
from solana.rpc.api import Client

# Page configuration
st.set_page_config(
    page_title="PSI-Coin Monitor | EVE 1010_WAKE",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
TOKEN_ADDRESS = "7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump"
WALLET_ADDRESS = "b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH"
SOLANA_RPC = "https://api.mainnet-beta.solana.com"
SOLSCAN_API_BASE = "https://public-api.solscan.io"

# Environment variables - SECURE: No hardcoded keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GROQ_API_KEY:
    st.caption("🔑 API Key Loaded")

# Initialize Solana client
solana_client = Client(SOLANA_RPC)

# Caching functions
@st.cache_data(ttl=60)
def fetch_token_metadata(token_address):
    """Fetch token metadata from Solscan API"""
    try:
        url = f"{SOLSCAN_API_BASE}/token/meta"
        params = {"tokenAddress": token_address}
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        st.error(f"Error fetching token metadata: {e}")
        return None

@st.cache_data(ttl=30)
def fetch_wallet_balance(wallet_address):
    """Fetch wallet SOL balance from Solana blockchain"""
    try:
        response = solana_client.get_balance(wallet_address)
        if response.value is not None:
            # Convert lamports to SOL (1 SOL = 1,000,000,000 lamports)
            balance_sol = response.value / 1_000_000_000
            return balance_sol
        return 0.0
    except Exception as e:
        st.error(f"Error fetching wallet balance: {e}")
        return 0.0

@st.cache_data(ttl=60)
def fetch_token_price(token_address):
    """Fetch token price from Solscan API"""
    try:
        url = f"{SOLSCAN_API_BASE}/market/token/{token_address}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("priceUsdt", 0.0)
        return 0.0
    except Exception as e:
        st.warning(f"Could not fetch token price: {e}")
        return 0.0

def load_csv_files():
    """Load CSV files from the repository root"""
    csv_files = []
    try:
        import glob
        csv_paths = glob.glob("*.csv")
        for csv_path in csv_paths:
            try:
                df = pd.read_csv(csv_path)
                csv_files.append({"name": csv_path, "data": df})
            except Exception as e:
                st.warning(f"Could not load {csv_path}: {e}")
    except Exception as e:
        st.warning(f"Error scanning for CSV files: {e}")
    return csv_files

def export_to_csv(data, filename):
    """Export data to CSV file"""
    try:
        df = pd.DataFrame(data)
        csv = df.to_csv(index=False)
        return csv
    except Exception as e:
        st.error(f"Error exporting to CSV: {e}")
        return None

# Main app
def main():
    # Header
    st.title("🚀 PSI-Coin Solana Blockchain Monitor")
    st.subheader("EVE 1010_WAKE - Real-Time Token & Wallet Tracking")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.write("**Token Address:**")
        st.code(TOKEN_ADDRESS, language=None)
        st.write("**Wallet Address:**")
        st.code(WALLET_ADDRESS, language=None)
        
        st.divider()
        
        # Auto-refresh toggle
        auto_refresh = st.checkbox("🔄 Auto-refresh (30s)", value=True)
        
        st.divider()
        
        # System info
        st.header("📊 System Status")
        st.metric("RPC Endpoint", "Solana Mainnet")
        st.metric("Update Interval", "30 seconds")
        st.caption(f"Last updated: {datetime.now().strftime('%H:%M:%S')}")
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Live Data", "💰 Holdings", "📁 CSV Data", "ℹ️ About"])
    
    with tab1:
        st.header("Live Blockchain Data")
        
        # Create columns for metrics
        col1, col2, col3 = st.columns(3)
        
        # Fetch wallet balance
        with col1:
            with st.spinner("Fetching wallet balance..."):
                wallet_balance = fetch_wallet_balance(WALLET_ADDRESS)
                st.metric(
                    label="💎 Wallet SOL Balance",
                    value=f"{wallet_balance:.4f} SOL",
                    delta=None
                )
        
        # Fetch token metadata
        with col2:
            with st.spinner("Fetching token data..."):
                token_metadata = fetch_token_metadata(TOKEN_ADDRESS)
                if token_metadata:
                    token_name = token_metadata.get("name", "PSI-Coin")
                    token_symbol = token_metadata.get("symbol", "PSI")
                    st.metric(
                        label="🪙 Token Info",
                        value=f"{token_symbol}",
                        delta=token_name
                    )
                else:
                    st.metric(
                        label="🪙 Token Info",
                        value="PSI-Coin",
                        delta="Loading..."
                    )
        
        # Fetch token price
        with col3:
            with st.spinner("Fetching token price..."):
                token_price = fetch_token_price(TOKEN_ADDRESS)
                st.metric(
                    label="💵 Token Price",
                    value=f"${token_price:.6f}" if token_price > 0 else "N/A",
                    delta=None
                )
        
        st.divider()
        
        # Token details
        if token_metadata:
            st.subheader("Token Metadata")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Name:**", token_metadata.get("name", "N/A"))
                st.write("**Symbol:**", token_metadata.get("symbol", "N/A"))
                st.write("**Decimals:**", token_metadata.get("decimals", "N/A"))
            
            with col2:
                st.write("**Token Type:**", "SPL Token")
                st.write("**Network:**", "Solana Mainnet")
                st.write("**Status:**", "✅ Active")
    
    with tab2:
        st.header("Holdings & Valuation")
        
        # Calculate holdings if we have price data
        token_price = fetch_token_price(TOKEN_ADDRESS)
        
        if token_price > 0:
            st.info("💡 Enter your PSI-Coin holdings to calculate current valuation")
            
            holdings_amount = st.number_input(
                "Enter PSI-Coin Amount:",
                min_value=0.0,
                value=0.0,
                step=1.0,
                format="%.2f"
            )
            
            if holdings_amount > 0:
                total_value = holdings_amount * token_price
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Holdings", f"{holdings_amount:,.2f} PSI")
                with col2:
                    st.metric("Token Price", f"${token_price:.6f}")
                with col3:
                    st.metric("Total Value", f"${total_value:.2f}")
                
                # Export option
                if st.button("💾 Export Holdings to CSV"):
                    export_data = [{
                        "Token": "PSI-Coin",
                        "Address": TOKEN_ADDRESS,
                        "Holdings": holdings_amount,
                        "Price_USD": token_price,
                        "Total_Value_USD": total_value,
                        "Timestamp": datetime.now().isoformat()
                    }]
                    csv_data = export_to_csv(export_data, "psi_holdings.csv")
                    if csv_data:
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_data,
                            file_name=f"psi_holdings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                        st.success("✅ Holdings data ready for download!")
        else:
            st.warning("⚠️ Token price data not available. Holdings calculation unavailable.")
    
    with tab3:
        st.header("CSV Data Management")
        
        # Load CSV files
        csv_files = load_csv_files()
        
        if csv_files:
            st.success(f"✅ Found {len(csv_files)} CSV file(s)")
            
            for csv_file in csv_files:
                with st.expander(f"📄 {csv_file['name']}", expanded=True):
                    st.dataframe(csv_file['data'], use_container_width=True)
                    
                    # Show statistics
                    st.caption(f"Rows: {len(csv_file['data'])} | Columns: {len(csv_file['data'].columns)}")
        else:
            st.info("ℹ️ No CSV files found in the repository root directory.")
            st.write("To add CSV data:")
            st.write("1. Place your `pump.fun.csv` or other CSV files in the root directory")
            st.write("2. Refresh the app to load the data")
            
        st.divider()
        
        # File upload option
        st.subheader("Upload CSV Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success(f"✅ Successfully loaded {uploaded_file.name}")
                st.dataframe(df, use_container_width=True)
                st.caption(f"Rows: {len(df)} | Columns: {len(df.columns)}")
            except Exception as e:
                st.error(f"❌ Error loading file: {e}")
    
    with tab4:
        st.header("About PSI-Coin Monitor")
        
        st.markdown("""
        ### 🎯 Purpose
        This application provides real-time monitoring of PSI-Coin (EVE 1010_WAKE) on the Solana blockchain.
        
        ### ✨ Features
        - **Real-time Data**: Live updates every 30 seconds
        - **Wallet Monitoring**: Track SOL balance in real-time
        - **Token Tracking**: Monitor PSI-Coin metadata and pricing
        - **CSV Integration**: Import and manage pump.fun.csv data
        - **Holdings Calculator**: Calculate portfolio valuation
        - **Data Export**: Export holdings and metrics to CSV
        
        ### 🔗 Blockchain Details
        - **Network**: Solana Mainnet Beta
        - **RPC Endpoint**: `api.mainnet-beta.solana.com`
        - **Token Standard**: SPL Token
        - **Data Source**: Solscan Public API
        
        ### 🔒 Security
        - ✅ No hardcoded API keys
        - ✅ Environment variable configuration
        - ✅ Read-only blockchain access
        - ✅ Public address monitoring only
        
        ### 📚 Resources
        - [Solana Documentation](https://docs.solana.com/)
        - [Solscan Explorer](https://solscan.io/)
        - [Streamlit Documentation](https://docs.streamlit.io/)
        """)
        
        st.divider()
        
        st.caption("Built with ❤️ using Streamlit | Version 1.0.0")
    
    # Auto-refresh mechanism
    if auto_refresh:
        time.sleep(30)
        st.rerun()

if __name__ == "__main__":
    main()
