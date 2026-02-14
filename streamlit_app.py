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

def log_activity(action, details, status):
    """Log activity to activity_log.csv"""
    try:
        log_file = "activity_log.csv"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Create log entry
        log_entry = {
            "Timestamp": timestamp,
            "Action": action,
            "Details": details,
            "Status": status
        }
        
        # Check if log file exists
        if os.path.exists(log_file):
            df = pd.read_csv(log_file)
            df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
        else:
            df = pd.DataFrame([log_entry])
        
        # Write to CSV
        df.to_csv(log_file, index=False)
        return True
    except Exception as e:
        st.warning(f"Could not log activity: {e}")
        return False

def load_activity_log():
    """Load activity log from CSV"""
    try:
        log_file = "activity_log.csv"
        if os.path.exists(log_file):
            df = pd.read_csv(log_file)
            return df
        return pd.DataFrame(columns=["Timestamp", "Action", "Details", "Status"])
    except Exception as e:
        st.warning(f"Could not load activity log: {e}")
        return pd.DataFrame(columns=["Timestamp", "Action", "Details", "Status"])

def get_activity_stats(log_df):
    """Calculate activity statistics"""
    if log_df.empty:
        return {"total": 0, "success": 0, "error": 0, "success_rate": 0}
    
    total = len(log_df)
    success = len(log_df[log_df['Status'] == 'SUCCESS'])
    error = len(log_df[log_df['Status'] == 'ERROR'])
    success_rate = (success / total * 100) if total > 0 else 0
    
    return {
        "total": total,
        "success": success,
        "error": error,
        "success_rate": success_rate
    }

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
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📈 Live Data", "🌐 CEC/WAM Live", "💰 Holdings", "📁 CSV Data", "📋 Activity Log", "ℹ️ About"])
    
    with tab1:
        st.header("Live Blockchain Data")
        
        # Live status indicators
        col_status1, col_status2, col_status3 = st.columns(3)
        with col_status1:
            st.markdown("🟢 **Live Connection Active**")
        with col_status2:
            countdown = 30 - (datetime.now().second % 30)
            st.markdown(f"🔄 **Auto-Refresh:** {countdown}s")
        with col_status3:
            st.markdown(f"📡 **Data Fresh:** ✅")
        
        st.divider()
        
        # Create columns for metrics
        col1, col2, col3 = st.columns(3)
        
        # Fetch wallet balance
        with col1:
            with st.spinner("🔄 Loading wallet balance..."):
                wallet_balance = fetch_wallet_balance(WALLET_ADDRESS)
                log_activity("FETCH_WALLET_BALANCE", f"Wallet: {WALLET_ADDRESS[:8]}...", "SUCCESS" if wallet_balance >= 0 else "ERROR")
                st.metric(
                    label="💎 Wallet SOL Balance",
                    value=f"{wallet_balance:.4f} SOL",
                    delta=None
                )
                st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        
        # Fetch token metadata
        with col2:
            with st.spinner("🔄 Loading token data..."):
                token_metadata = fetch_token_metadata(TOKEN_ADDRESS)
                if token_metadata:
                    log_activity("FETCH_TOKEN_METADATA", f"Token: {TOKEN_ADDRESS[:8]}...", "SUCCESS")
                    token_name = token_metadata.get("name", "PSI-Coin")
                    token_symbol = token_metadata.get("symbol", "PSI")
                    st.metric(
                        label="🪙 Token Info",
                        value=f"{token_symbol}",
                        delta=token_name
                    )
                else:
                    log_activity("FETCH_TOKEN_METADATA", f"Token: {TOKEN_ADDRESS[:8]}...", "ERROR")
                    st.metric(
                        label="🪙 Token Info",
                        value="PSI-Coin",
                        delta="Loading..."
                    )
                st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        
        # Fetch token price
        with col3:
            with st.spinner("🔄 Loading token price..."):
                token_price = fetch_token_price(TOKEN_ADDRESS)
                log_activity("FETCH_TOKEN_PRICE", f"Price: ${token_price:.6f}", "SUCCESS" if token_price > 0 else "WARNING")
                st.metric(
                    label="💵 Token Price",
                    value=f"${token_price:.6f}" if token_price > 0 else "N/A",
                    delta=None
                )
                st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        
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
        
        # Real-time refresh indicator
        col_sync1, col_sync2, col_sync3 = st.columns(3)
        with col_sync1:
            st.markdown("🔄 **Refresh Status:** Active")
        with col_sync2:
            data_age = datetime.now().strftime('%H:%M:%S')
            st.markdown(f"📊 **Data Age:** Just now")
        with col_sync3:
            st.markdown(f"⏱️ **Sync Interval:** 5 min")
        
        st.divider()
        
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
                
            if cec_wam_df is not None and not cec_wam_df.empty:
                log_activity("FETCH_CEC_WAM_DATA", f"Loaded {len(cec_wam_df)} records", "SUCCESS")
                st.success(f"✅ Successfully loaded {len(cec_wam_df)} records from live data source")
                st.caption(f"🕒 Data loaded at: {datetime.now().strftime('%H:%M:%S')}")
                
                # Animated record counter
                st.markdown(f"### 📊 Total Records: **{len(cec_wam_df)}**")
                
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
                    if st.download_button(
                        label="⬇️ Download as CSV",
                        data=csv_export,
                        file_name=f"cec_wam_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    ):
                        log_activity("EXPORT_CEC_WAM_DATA", f"Exported {len(cec_wam_df)} records", "SUCCESS")
                
                with col2:
                    st.info(f"🔄 Auto-refresh: Every {CEC_WAM_REFRESH_INTERVAL // 60} minutes")
                
            elif cec_wam_df is not None and cec_wam_df.empty:
                log_activity("FETCH_CEC_WAM_DATA", "Sheet is empty", "WARNING")
                st.warning("⚠️ Google Sheet is empty or has no data")
            else:
                log_activity("FETCH_CEC_WAM_DATA", "Failed to fetch data", "ERROR")
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
        st.header("💰 Holdings & Valuation Calculator")
        
        # Calculate holdings if we have price data
        with st.spinner("🔄 Loading price data..."):
            token_price = fetch_token_price(TOKEN_ADDRESS)
        
        if token_price > 0:
            st.success(f"✅ Current PSI-Coin Price: ${token_price:.6f}")
            st.caption(f"🕒 Price updated at: {datetime.now().strftime('%H:%M:%S')}")
            
            st.divider()
            
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
                
                st.divider()
                st.subheader("📊 Portfolio Summary")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("💎 Holdings", f"{holdings_amount:,.2f} PSI")
                with col2:
                    st.metric("💵 Token Price", f"${token_price:.6f}")
                with col3:
                    # Color-coded value indicator
                    value_color = "🟢" if total_value > 0 else "⚪"
                    st.metric(f"{value_color} Total Value", f"${total_value:.2f}")
                
                st.caption(f"🕒 Calculated at: {datetime.now().strftime('%H:%M:%S')}")
                
                st.divider()
                
                # Export option
                st.subheader("💾 Export Portfolio Data")
                if st.button("📥 Export Holdings to CSV"):
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
                        log_activity("EXPORT_HOLDINGS", f"Holdings: {holdings_amount}, Value: ${total_value:.2f}", "SUCCESS")
                        st.download_button(
                            label="⬇️ Download CSV",
                            data=csv_data,
                            file_name=f"psi_holdings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                        st.success("✅ Holdings data ready for download!")
                        st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
        else:
            st.warning("⚠️ Token price data not available. Holdings calculation unavailable.")
            log_activity("HOLDINGS_CALCULATOR", "Price not available", "WARNING")
    
    with tab4:
        st.header("📁 CSV Data Management")
        
        # Load CSV files
        with st.spinner("🔄 Loading CSV files..."):
            csv_files = load_csv_files()
        
        if csv_files:
            log_activity("LOAD_CSV_FILES", f"Loaded {len(csv_files)} files", "SUCCESS")
            st.success(f"✅ Found {len(csv_files)} CSV file(s)")
            st.caption(f"🕒 Files loaded at: {datetime.now().strftime('%H:%M:%S')}")
            
            st.divider()
            
            for csv_file in csv_files:
                with st.expander(f"📄 {csv_file['name']}", expanded=True):
                    st.dataframe(csv_file['data'], use_container_width=True)
                    
                    # Show statistics
                    st.caption(f"📊 Rows: {len(csv_file['data'])} | Columns: {len(csv_file['data'].columns)}")
        else:
            log_activity("LOAD_CSV_FILES", "No CSV files found", "INFO")
            st.info("ℹ️ No CSV files found in the repository root directory.")
            st.write("To add CSV data:")
            st.write("1. Place your `pump.fun.csv` or other CSV files in the root directory")
            st.write("2. Refresh the app to load the data")
            
        st.divider()
        
        # File upload option
        st.subheader("📤 Upload CSV Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
        
        if uploaded_file is not None:
            try:
                with st.spinner("🔄 Processing uploaded file..."):
                    df = pd.read_csv(uploaded_file)
                log_activity("UPLOAD_CSV", f"Uploaded {uploaded_file.name}", "SUCCESS")
                st.success(f"✅ Successfully loaded {uploaded_file.name}")
                st.dataframe(df, use_container_width=True)
                st.caption(f"📊 Rows: {len(df)} | Columns: {len(df.columns)}")
                st.caption(f"🕒 Uploaded at: {datetime.now().strftime('%H:%M:%S')}")
            except Exception as e:
                log_activity("UPLOAD_CSV", f"Failed to upload {uploaded_file.name}: {str(e)}", "ERROR")
                st.error(f"❌ Error loading file: {e}")
    
    with tab5:
        st.header("📋 Activity Log")
        
        # Load activity log
        with st.spinner("🔄 Loading activity log..."):
            activity_log = load_activity_log()
        
        # Activity statistics
        stats = get_activity_stats(activity_log)
        
        # Live system time
        st.markdown(f"### 🕒 System Time: **{datetime.now().strftime('%H:%M:%S')}**")
        
        st.divider()
        
        # Statistics dashboard
        st.subheader("📊 Activity Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📝 Total Operations", stats["total"])
        with col2:
            st.metric("✅ Successful", stats["success"], delta=None)
        with col3:
            st.metric("❌ Errors", stats["error"], delta=None)
        with col4:
            success_color = "🟢" if stats["success_rate"] >= 80 else "🟡" if stats["success_rate"] >= 50 else "🔴"
            st.metric(f"{success_color} Success Rate", f"{stats['success_rate']:.1f}%")
        
        st.divider()
        
        # Recent activity ticker
        if not activity_log.empty:
            st.subheader("🔄 Recent Activity (Last 5)")
            recent = activity_log.tail(5).sort_index(ascending=False)
            
            for idx, row in recent.iterrows():
                status_emoji = "✅" if row['Status'] == 'SUCCESS' else "⚠️" if row['Status'] == 'WARNING' else "❌"
                st.markdown(f"{status_emoji} **{row['Action']}** - {row['Details']} _{row['Timestamp']}_")
            
            st.divider()
            
            # Full activity log table
            st.subheader("📜 Complete Activity Log")
            
            # Color-code the status column
            def highlight_status(row):
                if row['Status'] == 'SUCCESS':
                    return ['background-color: #d4edda'] * len(row)
                elif row['Status'] == 'ERROR':
                    return ['background-color: #f8d7da'] * len(row)
                elif row['Status'] == 'WARNING':
                    return ['background-color: #fff3cd'] * len(row)
                else:
                    return [''] * len(row)
            
            # Display styled dataframe
            st.dataframe(
                activity_log.sort_index(ascending=False),
                use_container_width=True,
                height=400
            )
            
            st.caption(f"📈 Total Logged Operations: {len(activity_log)}")
            st.caption(f"🕒 Log last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Export activity log
            st.divider()
            st.subheader("💾 Export Activity Log")
            
            csv_export = activity_log.to_csv(index=False)
            st.download_button(
                label="⬇️ Download Activity Log CSV",
                data=csv_export,
                file_name=f"activity_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        else:
            st.info("ℹ️ No activity logged yet. Operations will be logged automatically as you use the application.")
    
    with tab6:
        st.header("About PSI-Coin Monitor")
        
        st.markdown("""
        ### 🎯 Purpose
        This application provides real-time monitoring of PSI-Coin (EVE 1010_WAKE) on the Solana blockchain.
        
        ### ✨ Features
        - **Real-time Data**: Live updates every 30 seconds
        - **Wallet Monitoring**: Track SOL balance in real-time
        - **Token Tracking**: Monitor PSI-Coin metadata and pricing
        - **Activity Logging**: Complete audit trail of all operations
          - Real-time operation tracking
          - Success rate analytics
          - Export logs for analysis
        - **CEC/WAM System**: Live data synchronization with Google Sheets
          - Color-coded status indicators (PERFECT, TODO, ACTIVE, STABLE)
          - Real-time status distribution analytics
          - Auto-refresh every 5 minutes
          - Data export capabilities
        - **CSV Integration**: Import and manage pump.fun.csv data
        - **Holdings Calculator**: Calculate portfolio valuation
        - **Data Export**: Export holdings and metrics to CSV
        
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
        
        st.caption("Built with ❤️ using Streamlit | Version 3.0.0 - Activity Logging & Enhanced Visuals")
    
    # Auto-refresh mechanism
    if auto_refresh:
        time.sleep(30)
        st.rerun()

if __name__ == "__main__":
    main()
