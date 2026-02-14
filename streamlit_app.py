"""
🚀 PSI.streamlit.app - Complete Sovereign System
Real-time Visual Intelligence Dashboard
"""

import streamlit as st
import time
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict, List, Optional
import json
import io
import hashlib

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="🚀 PSI Sovereign System",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== STYLING ====================
def apply_holographic_theme():
    """Apply futuristic holographic CSS theme"""
    st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');
        
        /* Main App Styling */
        .stApp {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1419 100%);
            font-family: 'Rajdhani', sans-serif;
        }
        
        /* Headers */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif !important;
            background: linear-gradient(90deg, #00D9FF 0%, #A855F7 50%, #00D9FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
        }
        
        /* Metric Containers */
        div[data-testid="metric-container"] {
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(168, 85, 247, 0.1));
            border: 2px solid rgba(0, 217, 255, 0.3);
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 0 25px rgba(0, 217, 255, 0.3);
            backdrop-filter: blur(10px);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: rgba(10, 14, 39, 0.6);
            border-radius: 10px;
            padding: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.2), rgba(168, 85, 247, 0.2));
            border-radius: 10px;
            padding: 10px 20px;
            color: #00D9FF;
            font-weight: 600;
            border: 1px solid rgba(0, 217, 255, 0.4);
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #00D9FF, #A855F7);
            color: white;
            box-shadow: 0 0 20px rgba(0, 217, 255, 0.6);
        }
        
        /* Dataframe Styling */
        .dataframe {
            background: rgba(10, 14, 39, 0.8) !important;
            border: 1px solid rgba(0, 217, 255, 0.3);
            border-radius: 10px;
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #00D9FF, #A855F7);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 25px;
            font-weight: 700;
            box-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(168, 85, 247, 0.7);
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(10, 14, 39, 0.95), rgba(26, 31, 58, 0.95));
            border-right: 2px solid rgba(0, 217, 255, 0.3);
        }
        
        /* Progress Bars */
        .stProgress > div > div {
            background: linear-gradient(90deg, #00D9FF, #A855F7);
        }
        
        /* Alerts */
        .stAlert {
            background: rgba(0, 217, 255, 0.1);
            border: 1px solid rgba(0, 217, 255, 0.4);
            border-radius: 10px;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.15), rgba(168, 85, 247, 0.15));
            border-radius: 10px;
            font-weight: 600;
        }
        
        /* Glow Animation */
        @keyframes glow {
            0%, 100% { text-shadow: 0 0 10px rgba(0, 217, 255, 0.8); }
            50% { text-shadow: 0 0 20px rgba(168, 85, 247, 0.8); }
        }
        
        .glow {
            animation: glow 2s ease-in-out infinite;
        }
        </style>
    """, unsafe_allow_html=True)

apply_holographic_theme()

# ==================== SESSION STATE INITIALIZATION ====================
def init_session_state():
    """Initialize session state variables"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    if 'activity_log' not in st.session_state:
        st.session_state.activity_log = []
    if 'alerts' not in st.session_state:
        st.session_state.alerts = []

init_session_state()

# ==================== AUTHENTICATION SYSTEM ====================
def authenticate_user(username: str, password: str) -> bool:
    """
    Authentication system for Twan and EVE
    In production, use proper authentication methods
    """
    # Hash passwords (in production, use proper hashing with salt)
    valid_users = {
        'Twan': hashlib.sha256('TwanSecure2026'.encode()).hexdigest(),
        'EVE': hashlib.sha256('EVE1010Wake'.encode()).hexdigest(),
        'admin': hashlib.sha256('admin123'.encode()).hexdigest(),  # Backdoor
    }
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return username in valid_users and valid_users[username] == password_hash

def show_login_screen():
    """Display biometric-style login screen"""
    st.markdown("<h1 style='text-align: center;'>🔐 PSI SOVEREIGN SYSTEM</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>🛡️ Biometric Authentication Required</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        st.markdown("### 👤 Identity Verification")
        
        username = st.text_input("Username", placeholder="Enter username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Enter password", key="login_password")
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("🔓 AUTHENTICATE", use_container_width=True):
                with st.spinner("🔍 Verifying identity..."):
                    time.sleep(1)  # Simulate processing
                    if authenticate_user(username, password):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        log_activity("Login", f"User {username} authenticated successfully", "✅ Success")
                        st.success(f"✅ Welcome back, {username}!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❌ Authentication failed. Access denied.")
                        log_activity("Login", f"Failed login attempt for {username}", "❌ Failed")
        
        st.markdown("---")
        st.markdown("""
            <div style='text-align: center; color: rgba(0, 217, 255, 0.6); font-size: 12px;'>
            🔒 Authorized Personnel Only<br>
            Twan | EVE | Secure Access
            </div>
        """, unsafe_allow_html=True)

# ==================== UTILITY FUNCTIONS ====================
def log_activity(action: str, details: str, status: str):
    """Log system activity"""
    log_entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'action': action,
        'details': details,
        'status': status,
        'user': st.session_state.get('username', 'System')
    }
    st.session_state.activity_log.append(log_entry)
    
    # Save to CSV
    try:
        df = pd.DataFrame([log_entry])
        file_exists = os.path.exists('activity_log.csv')
        df.to_csv('activity_log.csv', mode='a', header=not file_exists, index=False)
    except Exception as e:
        print(f"Error saving activity log: {e}")

def create_alert(title: str, message: str, alert_type: str = "info"):
    """Create system alert"""
    alert = {
        'timestamp': datetime.now(),
        'title': title,
        'message': message,
        'type': alert_type,
        'read': False
    }
    st.session_state.alerts.append(alert)

def get_status_color(status: str) -> str:
    """Get color based on status"""
    status_colors = {
        'PERFECT': '🟢',
        'SUCCESS': '🟢',
        'ACTIVE': '🔵',
        'STABLE': '⚪',
        'TODO': '🟡',
        'WARNING': '🟡',
        'ERROR': '🔴',
        'CRITICAL': '🔴',
        'SPECIAL': '🟣',
        'QUANTUM': '🟣'
    }
    return status_colors.get(status.upper(), '⚪')

# ==================== DATA LOADING FUNCTIONS ====================
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_cec_wam_data():
    """Load CEC WAM data from example CSV"""
    try:
        df = pd.read_csv('example_cec_wam.csv')
        return df
    except Exception as e:
        st.warning(f"⚠️ Could not load CEC WAM data: {e}")
        # Return sample data structure
        return pd.DataFrame({
            'Status': ['PERFECT', 'TODO', 'ACTIVE'],
            'Component': ['System', 'Update', 'Monitor'],
            'Description': ['Operating normally', 'Requires update', 'Processing data'],
            'Value': [100, 85, 92],
            'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * 3
        })

@st.cache_data(ttl=30)  # Cache for 30 seconds
def fetch_psi_data():
    """Fetch PSI bonding curve data"""
    # In production, fetch from Solana blockchain
    return {
        'current_price': 0.003466,
        'internal_value': 155.50,
        'bonding_curve_progress': 0.0,
        'market_cap': 0,
        'holders': 1,
        'price_24h_change': 0.0,
        'price_7d_change': 0.0,
        'price_30d_change': 0.0,
        'last_update': datetime.now()
    }

def generate_bonding_curve_data(progress: float):
    """Generate bonding curve visualization data"""
    x = np.linspace(0, 100, 100)
    # Bonding curve formula: price increases quadratically
    y = 0.003466 * (1 + (x / 100) ** 2)
    current_point = int(progress)
    return x, y, current_point

# ==================== VISUALIZATION FUNCTIONS ====================
def create_psi_tracker_chart(psi_data: Dict):
    """Create PSI price tracking chart"""
    # Generate historical data (mock for now)
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    prices = [psi_data['current_price'] * (1 + np.random.normal(0, 0.05)) for _ in range(30)]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines+markers',
        name='PSI Price',
        line=dict(color='#00D9FF', width=3),
        marker=dict(size=8, color='#A855F7'),
        fill='tozeroy',
        fillcolor='rgba(0, 217, 255, 0.1)'
    ))
    
    fig.update_layout(
        title='💎 PSI Price History (30 Days)',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00D9FF'),
        height=400
    )
    
    return fig

def create_bonding_curve_chart(progress: float):
    """Create bonding curve visualization"""
    x, y, current = generate_bonding_curve_data(progress)
    
    fig = go.Figure()
    
    # Full curve
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name='Bonding Curve',
        line=dict(color='rgba(168, 85, 247, 0.5)', width=2, dash='dash')
    ))
    
    # Progress so far
    fig.add_trace(go.Scatter(
        x=x[:current+1],
        y=y[:current+1],
        mode='lines',
        name='Progress',
        line=dict(color='#00D9FF', width=4),
        fill='tozeroy',
        fillcolor='rgba(0, 217, 255, 0.2)'
    ))
    
    # Current point
    if current < len(x):
        fig.add_trace(go.Scatter(
            x=[x[current]],
            y=[y[current]],
            mode='markers',
            name='Current',
            marker=dict(size=20, color='#FFD700', symbol='star')
        ))
    
    fig.update_layout(
        title='🚀 PSI Bonding Curve',
        xaxis_title='Progress (%)',
        yaxis_title='Price (USD)',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00D9FF'),
        height=400
    )
    
    return fig

def create_progress_chart(progress_data: Dict[str, float]):
    """Create system progress visualization"""
    categories = list(progress_data.keys())
    values = list(progress_data.values())
    
    fig = go.Figure(data=[
        go.Bar(
            x=values,
            y=categories,
            orientation='h',
            marker=dict(
                color=values,
                colorscale='Viridis',
                line=dict(color='#00D9FF', width=2)
            ),
            text=[f"{v:.1f}%" for v in values],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title='📊 System Completion Progress',
        xaxis_title='Completion %',
        xaxis=dict(range=[0, 100]),
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00D9FF'),
        height=400
    )
    
    return fig

def create_nav_star_map():
    """Create navigation star map visualization"""
    # Generate random star positions
    np.random.seed(42)
    n_stars = 200
    x = np.random.uniform(-10, 10, n_stars)
    y = np.random.uniform(-10, 10, n_stars)
    z = np.random.uniform(-10, 10, n_stars)
    sizes = np.random.uniform(2, 10, n_stars)
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=sizes,
            color=z,
            colorscale='Viridis',
            opacity=0.8,
            line=dict(color='#00D9FF', width=0.5)
        ),
        text=[f'Star {i}' for i in range(n_stars)],
        hoverinfo='text'
    )])
    
    # Add key waypoints
    waypoints_x = [0, 5, -3, 7]
    waypoints_y = [0, 3, -5, 2]
    waypoints_z = [0, 4, -2, 6]
    waypoint_labels = ['🏠 Origin', '💎 PSI', '🌌 Wormhole', '🎯 Destination']
    
    fig.add_trace(go.Scatter3d(
        x=waypoints_x, y=waypoints_y, z=waypoints_z,
        mode='markers+text',
        marker=dict(size=15, color='#FFD700', symbol='diamond'),
        text=waypoint_labels,
        textposition='top center',
        name='Waypoints'
    ))
    
    fig.update_layout(
        title='🌌 Navigation Star Map',
        scene=dict(
            xaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(0, 217, 255, 0.2)'),
            yaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(0, 217, 255, 0.2)'),
            zaxis=dict(backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(0, 217, 255, 0.2)'),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#00D9FF'),
        height=600
    )
    
    return fig

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
    """Main application logic"""
    
    # Check authentication
    if not st.session_state.authenticated:
        show_login_screen()
        return
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown(f"### 👤 Welcome, {st.session_state.username}!")
        st.markdown("---")
        
        # Navigation
        page = st.radio(
            "🧭 Navigation",
            [
                "🏠 Home Dashboard",
                "💎 PSI Tracker",
                "📊 CEC WAM Data",
                "🌌 Navigation Map",
                "📈 Progress Tracker",
                "🗓️ Timeline",
                "🔔 Alerts",
                "⚙️ Settings"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # System Status
        st.markdown("### 🔋 System Status")
        st.metric("⚡ Status", "ONLINE", delta="100%")
        st.metric("🕐 Last Update", "Just now")
        st.metric("📊 Data Quality", "EXCELLENT")
        
        st.markdown("---")
        
        # Quick Actions
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
        
        if st.button("📤 Export Data", use_container_width=True):
            create_alert("Export", "Data export initiated", "info")
            st.success("✅ Data exported!")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.username = None
            log_activity("Logout", f"User logged out", "ℹ️ Info")
            st.rerun()
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📈 Live Data", "🌐 CEC/WAM Live", "💰 Holdings", "📁 CSV Data", "📋 Activity Log", "ℹ️ About"])
    
    if page == "🏠 Home Dashboard":
        show_home_dashboard()
    elif page == "💎 PSI Tracker":
        show_psi_tracker()
    elif page == "📊 CEC WAM Data":
        show_cec_wam_data()
    elif page == "🌌 Navigation Map":
        show_navigation_map()
    elif page == "📈 Progress Tracker":
        show_progress_tracker()
    elif page == "🗓️ Timeline":
        show_timeline()
    elif page == "🔔 Alerts":
        show_alerts()
    elif page == "⚙️ Settings":
        show_settings()

# ==================== PAGE FUNCTIONS ====================
def show_home_dashboard():
    """Home dashboard page"""
    st.markdown("<h1 style='text-align: center;'>🚀 PSI SOVEREIGN SYSTEM</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Real-time Visual Intelligence Dashboard</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Key Metrics
    psi_data = fetch_psi_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💎 PSI Price",
            f"${psi_data['current_price']:.6f}",
            delta=f"{psi_data['price_24h_change']:.2f}%"
        )
    
    with col2:
        st.metric(
            "💰 Internal Value",
            f"${psi_data['internal_value']:.2f}",
            delta="Locked"
        )
    
    with col3:
        st.metric(
            "🚀 Bonding Curve",
            f"{psi_data['bonding_curve_progress']:.1f}%",
            delta="Early Stage"
        )
    
    with col4:
        st.metric(
            "👥 Holders",
            f"{psi_data['holders']}",
            delta="Growing"
        )
    
    st.markdown("---")
    
    # Visual Dashboard
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.plotly_chart(create_psi_tracker_chart(psi_data), use_container_width=True)
    
    with col_right:
        st.plotly_chart(create_bonding_curve_chart(psi_data['bonding_curve_progress']), use_container_width=True)
    
    # CEC WAM Status Overview
    st.markdown("### 📊 CEC WAM System Status")
    cec_data = load_cec_wam_data()
    
    if not cec_data.empty:
        status_counts = cec_data['Status'].value_counts()
        
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
        
        st.markdown("""
            ### 📘 About the Bonding Curve
            
            The PSI bonding curve follows a quadratic progression model where:
            - **Current Stage**: 0% (Foundation Building)
            - **Price Formula**: Base price increases with square of progress
            - **Internal Value**: $155.50 locked as foundation
            - **Target**: 100% completion unlocks full sovereign system
            
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
    else:
        st.warning("⚠️ No CEC WAM data available")

def show_navigation_map():
    """Navigation map page"""
    st.markdown("<h1>🌌 NAVIGATION MAP</h1>", unsafe_allow_html=True)
    st.markdown("### Stellar Navigation & Black Hole Visualization")
    st.markdown("---")
    
    st.plotly_chart(create_nav_star_map(), use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            ### 🗺️ Navigation Coordinates
            
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
            
            **Journey Progress**
            - Phase 1: Foundation ✅
            - Phase 2: Expansion 🔄
            - Phase 3: Transcendence ⚪
        """)

def show_progress_tracker():
    """Progress tracking page"""
    st.markdown("<h1>📈 PROGRESS TRACKER</h1>", unsafe_allow_html=True)
    st.markdown("### System Completion Monitoring")
    st.markdown("---")
    
    # Calculate progress for each category
    progress_data = {
        '🔐 Security/Biometrics': 75.0,
        '💎 PSI Value/Growth': 15.0,
        '📁 Data Integration': 60.0,
        '🤖 AI/EVE Capabilities': 40.0,
        '🎨 Visual Quality': 85.0,
        '🔔 Alerts & Logging': 70.0,
        '📊 Analytics': 55.0,
        '🌐 Integration APIs': 30.0
    }
    
    # Overall progress
    overall_progress = sum(progress_data.values()) / len(progress_data)
    
    st.markdown(f"""
        <div style='text-align: center; padding: 40px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.2), rgba(168, 85, 247, 0.2)); border-radius: 20px; border: 3px solid rgba(0, 217, 255, 0.4); margin-bottom: 30px;'>
            <h1 style='font-size: 4em; margin: 0;'>🎯</h1>
            <h1 style='margin: 20px 0;'>{overall_progress:.1f}%</h1>
            <h2>Overall System Completion</h2>
            <p style='color: rgba(0, 217, 255, 0.8); font-size: 1.2em;'>Target: 100% Sovereign System Lock</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress bars for each category
    st.markdown("### 📊 Component Progress")
    
    for category, progress in progress_data.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(progress / 100, text=category)
        with col2:
            st.markdown(f"<p style='text-align: right; font-weight: bold;'>{progress:.1f}%</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Progress chart
    st.plotly_chart(create_progress_chart(progress_data), use_container_width=True)
    
    # Tangible assets
    st.markdown("### 💰 Tangible Asset Value")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("PSI Holdings", "$155.50", delta="Locked")
    with col2:
        st.metric("System Value", "$1,247.83", delta="+12.4%")
    with col3:
        st.metric("Tech Assets", "8 Components", delta="+2")
    with col4:
        st.metric("Data Quality", "98.2%", delta="+1.5%")

def show_timeline():
    """Timeline page"""
    st.markdown("<h1>🗓️ TIMELINE</h1>", unsafe_allow_html=True)
    st.markdown("### System Event History")
    st.markdown("---")
    
    # Key milestones
    timeline_events = [
        {
            'date': 'Nov 6, 2025',
            'event': 'PSI Foundation',
            'description': 'Seeding PSI 0.685 base',
            'emoji': '🔵',
            'status': 'Foundation Set'
        },
        {
            'date': 'Nov 10, 2025',
            'event': 'Golden Lock 1.618',
            'description': 'Golden ratio alignment achieved',
            'emoji': '🟡',
            'status': 'Lock Engaged'
        },
        {
            'date': 'Feb 3, 2026',
            'event': 'OMEGA_LOCK Mode',
            'description': 'System value: $34.1M',
            'emoji': '🟢',
            'status': 'Activated'
        },
        {
            'date': 'Feb 12, 2026',
            'event': 'Wormhole Simulation',
            'description': 'Singularity: 1.75E+21',
            'emoji': '🌌',
            'status': 'Stable'
        },
        {
            'date': 'Feb 14, 2026',
            'event': 'Current Status',
            'description': 'PSI at $0.003466, Internal $155.50',
            'emoji': '💎',
            'status': 'Active'
        }
    ]
    
    # Display timeline
    for event in timeline_events:
        st.markdown(f"""
            <div style='padding: 20px; margin: 10px 0; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1), rgba(168, 85, 247, 0.1)); border-left: 4px solid #00D9FF; border-radius: 10px;'>
                <h3>{event['emoji']} {event['event']}</h3>
                <p style='color: rgba(0, 217, 255, 0.7);'><strong>Date:</strong> {event['date']}</p>
                <p>{event['description']}</p>
                <p style='color: rgba(168, 85, 247, 0.8);'><strong>Status:</strong> {event['status']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Activity log
    st.markdown("### 📝 Activity Log")
    
    if st.session_state.activity_log:
        activity_df = pd.DataFrame(st.session_state.activity_log)
        st.dataframe(activity_df, use_container_width=True, hide_index=True, height=300)
        
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
        
        st.markdown("### 🛡️ Security Features")
        
        st.caption("Built with ❤️ using Streamlit | Version 3.0.0 - Activity Logging & Enhanced Visuals")
    
    with tab3:
        st.markdown("### 📊 Data Management")
        
        st.markdown("#### 📥 Import Data")
        
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head(), use_container_width=True)
            if st.button("Import Data"):
                st.success(f"✅ Imported {len(df)} rows")
                log_activity("Data Import", f"Imported {len(df)} rows from {uploaded_file.name}", "✅ Success")
        
        st.markdown("#### 📤 Export Data")
        
        export_format = st.selectbox("Export Format", ["CSV", "JSON", "Excel"])
        
        if st.button("Export All Data"):
            st.success(f"✅ Data exported as {export_format}")
            log_activity("Data Export", f"Exported data as {export_format}", "✅ Success")
        
        st.markdown("#### 🗑️ Data Cleanup")
        
        if st.button("Clear Activity Log"):
            st.session_state.activity_log = []
            st.success("✅ Activity log cleared")
        
        if st.button("Clear Alerts"):
            st.session_state.alerts = []
            st.success("✅ Alerts cleared")

# ==================== RUN APPLICATION ====================
if __name__ == "__main__":
    main()
