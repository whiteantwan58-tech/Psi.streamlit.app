import streamlit as st
import pandas as pd
import requests
import time
import os
import glob
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

# CEC/WAM System Constants
CEC_WAM_GOOGLE_SHEET_URL = os.getenv("CEC_WAM_SHEET_URL", "")
CEC_WAM_REFRESH_INTERVAL = 300  # 5 minutes in seconds
CEC_WAM_STATUS_COLORS = {
    "PERFECT": "🟢",
    "TODO": "🟡",
    "ACTIVE": "🔵",
    "STABLE": "⚪"
}

# Activity Logging Constants
ACTIVITY_LOG_FILE = "activity_log.csv"
ENABLE_AUTO_LOGGING = True

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

@st.cache_data(ttl=CEC_WAM_REFRESH_INTERVAL)
def fetch_cec_wam_data(sheet_url):
    """Fetch live data from Google Sheets CSV export for CEC/WAM system"""
    try:
        if not sheet_url:
            return None
        
        # Convert Google Sheets URL to CSV export URL
        if "/edit" in sheet_url:
            csv_url = sheet_url.replace("/edit", "/export?format=csv")
        elif "docs.google.com/spreadsheets/d/" in sheet_url:
            # Extract sheet ID and create CSV export URL
            sheet_id = sheet_url.split("/d/")[1].split("/")[0]
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        else:
            csv_url = sheet_url
        
        response = requests.get(csv_url, timeout=15)
        if response.status_code == 200:
            from io import StringIO
            df = pd.read_csv(StringIO(response.text))
            return df
        return None
    except Exception as e:
        st.error(f"Error fetching CEC/WAM data: {e}")
        return None

def analyze_cec_wam_status(df):
    """Analyze status distribution in CEC/WAM data"""
    if df is None or 'Status' not in df.columns:
        return {}
    
    status_counts = {}
    for status in ["PERFECT", "TODO", "ACTIVE", "STABLE"]:
        count = len(df[df['Status'].str.upper() == status]) if 'Status' in df.columns else 0
        status_counts[status] = count
    
    return status_counts

def get_status_indicator(status):
    """Get color indicator for status"""
    status_upper = str(status).upper()
    return CEC_WAM_STATUS_COLORS.get(status_upper, "⚫")

def log_activity(action, details="", status="SUCCESS"):
    """Log activity to CSV file for tracking"""
    if not ENABLE_AUTO_LOGGING:
        return
    
    try:
        log_entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "action": action,
            "details": details,
            "status": status
        }
        
        # Check if log file exists
        file_exists = os.path.exists(ACTIVITY_LOG_FILE)
        
        # Create or append to log file with proper error handling
        # Using mode='a' (append) with immediate flush for better thread safety
        df = pd.DataFrame([log_entry])
        
        # Write with explicit encoding and immediate flush
        with open(ACTIVITY_LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            df.to_csv(f, mode='a', header=not file_exists, index=False)
        
        return True
    except Exception as e:
        # Silent fail to not interrupt main app, but log to console for debugging
        print(f"Logging error: {e}")
        return False

def get_activity_log():
    """Read activity log from CSV"""
    try:
        if os.path.exists(ACTIVITY_LOG_FILE):
            df = pd.read_csv(ACTIVITY_LOG_FILE)
            return df
        return pd.DataFrame(columns=["timestamp", "action", "details", "status"])
    except Exception as e:
        st.warning(f"Could not load activity log: {e}")
        return pd.DataFrame(columns=["timestamp", "action", "details", "status"])

def load_csv_files():
    """Load CSV files from the repository root"""
    csv_files = []
    try:
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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Live Data", 
        "🌐 CEC/WAM Live", 
        "💰 Holdings", 
        "📁 CSV Data", 
        "📊 Activity Log",
        "ℹ️ About"
    ])
    
    with tab1:
        st.header("Live Blockchain Data")
        
        # Log data fetch
        log_activity("DATA_FETCH", "Fetching live blockchain data", "INITIATED")
        
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
                log_activity("WALLET_BALANCE", f"Balance: {wallet_balance:.4f} SOL", "SUCCESS")
        
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
                    log_activity("TOKEN_METADATA", f"Symbol: {token_symbol}, Name: {token_name}", "SUCCESS")
                else:
                    st.metric(
                        label="🪙 Token Info",
                        value="PSI-Coin",
                        delta="Loading..."
                    )
                    log_activity("TOKEN_METADATA", "Failed to fetch token metadata", "WARNING")
        
        # Fetch token price
        with col3:
            with st.spinner("Fetching token price..."):
                token_price = fetch_token_price(TOKEN_ADDRESS)
                st.metric(
                    label="💵 Token Price",
                    value=f"${token_price:.6f}" if token_price > 0 else "N/A",
                    delta=None
                )
                if token_price > 0:
                    log_activity("TOKEN_PRICE", f"Price: ${token_price:.6f}", "SUCCESS")
        
        # Visual separator with timestamp
        st.divider()
        col_time1, col_time2 = st.columns([3, 1])
        with col_time1:
            st.success("✅ Live data updated successfully")
        with col_time2:
            st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        
        # Log completion of data fetch
        log_activity("DATA_FETCH", "Live blockchain data fetched successfully", "SUCCESS")
        
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
        st.header("🌐 CEC/WAM Live Data System")
        
        st.info("📊 **CEC/WAM (Wide Area Monitoring)** - Real-time data synchronization system")
        
        # Configuration section
        with st.expander("⚙️ CEC/WAM Configuration", expanded=True):
            st.write("**Google Sheets URL Configuration:**")
            
            # Check if URL is configured
            if CEC_WAM_GOOGLE_SHEET_URL:
                st.success(f"✅ Sheet URL configured")
                st.code(CEC_WAM_GOOGLE_SHEET_URL[:50] + "..." if len(CEC_WAM_GOOGLE_SHEET_URL) > 50 else CEC_WAM_GOOGLE_SHEET_URL)
            else:
                st.warning("⚠️ No Google Sheets URL configured")
                st.write("To enable CEC/WAM live data:")
                st.markdown("""
                1. Set the `CEC_WAM_SHEET_URL` environment variable
                2. Use a Google Sheets URL (must be publicly accessible)
                3. Example: `https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit`
                """)
            
            st.write("**Status Color Codes:**")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"{CEC_WAM_STATUS_COLORS['PERFECT']} PERFECT")
            with col2:
                st.write(f"{CEC_WAM_STATUS_COLORS['TODO']} TODO")
            with col3:
                st.write(f"{CEC_WAM_STATUS_COLORS['ACTIVE']} ACTIVE")
            with col4:
                st.write(f"{CEC_WAM_STATUS_COLORS['STABLE']} STABLE")
        
        st.divider()
        
        # Fetch and display CEC/WAM data
        if CEC_WAM_GOOGLE_SHEET_URL:
            with st.spinner("🔄 Fetching live CEC/WAM data from Google Sheets..."):
                cec_wam_df = fetch_cec_wam_data(CEC_WAM_GOOGLE_SHEET_URL)
                log_activity("CEC_WAM_SYNC", f"Fetching data from Google Sheets", "INITIATED")
                
            if cec_wam_df is not None and not cec_wam_df.empty:
                st.success(f"✅ Successfully loaded {len(cec_wam_df)} records from live data source")
                log_activity("CEC_WAM_SYNC", f"Loaded {len(cec_wam_df)} records", "SUCCESS")
                
                # Status distribution analytics
                status_counts = analyze_cec_wam_status(cec_wam_df)
                
                if status_counts:
                    st.subheader("📊 Status Distribution")
                    cols = st.columns(4)
                    for idx, (status, count) in enumerate(status_counts.items()):
                        with cols[idx]:
                            st.metric(
                                label=f"{CEC_WAM_STATUS_COLORS[status]} {status}",
                                value=count
                            )
                
                st.divider()
                
                # Display the data with status indicators
                st.subheader("📋 Live CEC/WAM Data Table")
                
                # Add status indicators to dataframe display
                if 'Status' in cec_wam_df.columns:
                    display_df = cec_wam_df.copy()
                    display_df['Status'] = display_df['Status'].apply(
                        lambda x: f"{get_status_indicator(x)} {x}"
                    )
                    st.dataframe(display_df, use_container_width=True, height=400)
                else:
                    st.dataframe(cec_wam_df, use_container_width=True, height=400)
                
                # Data statistics
                st.caption(f"📈 Total Records: {len(cec_wam_df)} | Columns: {len(cec_wam_df.columns)} | Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Export option
                st.divider()
                st.subheader("💾 Export CEC/WAM Data")
                
                col1, col2 = st.columns(2)
                with col1:
                    csv_export = cec_wam_df.to_csv(index=False)
                    st.download_button(
                        label="⬇️ Download as CSV",
                        data=csv_export,
                        file_name=f"cec_wam_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
                
                with col2:
                    st.info(f"🔄 Auto-refresh: Every {CEC_WAM_REFRESH_INTERVAL // 60} minutes")
                
            elif cec_wam_df is not None and cec_wam_df.empty:
                st.warning("⚠️ Google Sheet is empty or has no data")
            else:
                st.error("❌ Failed to fetch CEC/WAM data. Please check:")
                st.markdown("""
                - Sheet URL is correct
                - Sheet is publicly accessible (Share → Anyone with link can view)
                - Sheet contains valid CSV data
                """)
        else:
            st.info("ℹ️ CEC/WAM live data system is not configured. Set `CEC_WAM_SHEET_URL` to enable.")
            
            # Demo/Example section
            with st.expander("📖 Learn More About CEC/WAM System"):
                st.markdown("""
                ### What is CEC/WAM?
                
                **CEC/WAM (Wide Area Monitoring)** is a real-time data monitoring and aggregation system that:
                
                - 🔄 **Live Data Sync**: Automatically fetches data from Google Sheets
                - 🎨 **Color-Coded Status**: Visual indicators for system states
                - 📊 **Analytics**: Real-time status distribution and metrics
                - 💾 **Data Export**: Export live data for offline analysis
                - ⚡ **Auto-Refresh**: Keeps data fresh with periodic updates
                
                ### Status System
                
                - 🟢 **PERFECT**: System operating optimally
                - 🟡 **TODO**: Items requiring attention
                - 🔵 **ACTIVE**: Currently processing or in progress
                - ⚪ **STABLE**: System in stable state
                
                ### Setup Instructions
                
                1. Create a Google Sheet with your data
                2. Make it publicly accessible (Share → Anyone with link can view)
                3. Set environment variable: `CEC_WAM_SHEET_URL=your_sheet_url`
                4. Restart the application
                
                ### Expected Data Format
                
                Your Google Sheet should include at least these columns:
                - **Status**: PERFECT, TODO, ACTIVE, or STABLE
                - Any additional columns for your data
                """)
    
    with tab3:
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
    
    with tab4:
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
    
    with tab5:
        st.header("📊 Activity Log & Auto-Logging")
        
        st.info("🔄 **Automatic Activity Logging** - All system activities are automatically logged to CSV")
        
        # Configuration
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📁 Log File", ACTIVITY_LOG_FILE)
        with col2:
            st.metric("🔄 Auto-Logging", "✅ ENABLED" if ENABLE_AUTO_LOGGING else "❌ DISABLED")
        
        st.divider()
        
        # Load and display activity log
        activity_df = get_activity_log()
        
        if not activity_df.empty:
            st.subheader("📋 Recent Activity")
            
            # Statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Entries", len(activity_df))
            with col2:
                success_count = len(activity_df[activity_df['status'] == 'SUCCESS'])
                st.metric("✅ Success", success_count)
            with col3:
                warning_count = len(activity_df[activity_df['status'] == 'WARNING'])
                st.metric("⚠️ Warnings", warning_count)
            with col4:
                error_count = len(activity_df[activity_df['status'] == 'ERROR'])
                st.metric("❌ Errors", error_count)
            
            st.divider()
            
            # Filter options
            st.subheader("🔍 Filter Logs")
            col1, col2 = st.columns(2)
            
            with col1:
                status_filter = st.multiselect(
                    "Filter by Status",
                    options=activity_df['status'].unique().tolist(),
                    default=activity_df['status'].unique().tolist()
                )
            
            with col2:
                action_filter = st.multiselect(
                    "Filter by Action",
                    options=activity_df['action'].unique().tolist(),
                    default=activity_df['action'].unique().tolist()
                )
            
            # Apply filters
            filtered_df = activity_df[
                (activity_df['status'].isin(status_filter)) &
                (activity_df['action'].isin(action_filter))
            ]
            
            # Display filtered data (most recent first)
            st.dataframe(
                filtered_df.sort_values('timestamp', ascending=False),
                use_container_width=True,
                height=400
            )
            
            st.caption(f"Showing {len(filtered_df)} of {len(activity_df)} log entries")
            
            # Export options
            st.divider()
            st.subheader("💾 Export Activity Log")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                csv_export = filtered_df.to_csv(index=False)
                st.download_button(
                    label="⬇️ Download Filtered Log",
                    data=csv_export,
                    file_name=f"activity_log_filtered_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            with col2:
                full_csv = activity_df.to_csv(index=False)
                st.download_button(
                    label="⬇️ Download Full Log",
                    data=full_csv,
                    file_name=f"activity_log_full_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            
            with col3:
                if st.button("🗑️ Clear Activity Log", type="secondary"):
                    try:
                        if os.path.exists(ACTIVITY_LOG_FILE):
                            os.remove(ACTIVITY_LOG_FILE)
                            st.success("✅ Activity log cleared!")
                            st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error clearing log: {e}")
            
        else:
            st.info("ℹ️ No activity logs yet. Start using the app to generate logs!")
            st.write("**Logged Activities Include:**")
            st.markdown("""
            - 📊 Data fetch operations
            - 💰 Wallet balance checks
            - 🪙 Token metadata queries
            - 💵 Price updates
            - 🌐 CEC/WAM data synchronization
            - 📁 CSV file operations
            - And more...
            """)
    
    with tab6:
        st.header("About PSI-Coin Monitor")
        
        st.markdown("""
        ### 🎯 Purpose
        This application provides real-time monitoring of PSI-Coin (EVE 1010_WAKE) on the Solana blockchain.
        
        ### ✨ Features
        - **Real-time Data**: Live updates every 30 seconds
        - **Wallet Monitoring**: Track SOL balance in real-time
        - **Token Tracking**: Monitor PSI-Coin metadata and pricing
        - **CEC/WAM System**: Live data synchronization with Google Sheets
          - Color-coded status indicators (PERFECT, TODO, ACTIVE, STABLE)
          - Real-time status distribution analytics
          - Auto-refresh every 5 minutes
          - Data export capabilities
        - **Activity Logging**: Automatic logging of all system activities to CSV
          - Real-time activity tracking
          - Filter and search capabilities
          - Export logs for analysis
          - Performance monitoring
        - **CSV Integration**: Import and manage pump.fun.csv data
        - **Holdings Calculator**: Calculate portfolio valuation
        - **Data Export**: Export holdings and metrics to CSV
        - **Enhanced Visuals**: Modern, responsive UI with real-time updates
        
        ### 🔗 Blockchain Details
        - **Network**: Solana Mainnet Beta
        - **RPC Endpoint**: `api.mainnet-beta.solana.com`
        - **Token Standard**: SPL Token
        - **Data Source**: Solscan Public API
        
        ### 🌐 CEC/WAM System
        - **Purpose**: Wide Area Monitoring for real-time data aggregation
        - **Data Source**: Google Sheets (CSV export)
        - **Refresh Rate**: 5 minutes (300 seconds)
        - **Status Codes**: PERFECT (🟢), TODO (🟡), ACTIVE (🔵), STABLE (⚪)
        - **Features**: Live sync, analytics, color-coded indicators, data export
        
        ### 📊 Activity Logging System
        - **Auto-Logging**: Automatically logs all system activities
        - **CSV Storage**: All logs saved to `activity_log.csv`
        - **Real-time Tracking**: Monitors data fetches, API calls, and user actions
        - **Analytics**: View statistics, filter logs, and export for analysis
        - **Performance**: Track system health and response times
        
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
        
        st.caption("Built with ❤️ using Streamlit | Version 2.1.0 - Enhanced with Auto-Logging & Visual Updates")
    
    # Auto-refresh mechanism
    if auto_refresh:
        time.sleep(30)
        st.rerun()

if __name__ == "__main__":
    main()
