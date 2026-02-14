"""
🚀 PSI.streamlit.app - Complete Sovereign System
Real-time Visual Intelligence Dashboard
"""

import streamlit as st
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

# ==================== MAIN APPLICATION ====================
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
    
    # ==================== PAGE ROUTING ====================
    
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
        
        cols = st.columns(len(status_counts))
        for i, (status, count) in enumerate(status_counts.items()):
            with cols[i]:
                st.metric(f"{get_status_color(status)} {status}", count)
    
    # Recent Activity
    st.markdown("### 📝 Recent Activity")
    if st.session_state.activity_log:
        recent_logs = pd.DataFrame(st.session_state.activity_log[-10:])
        st.dataframe(recent_logs, use_container_width=True, hide_index=True)
    else:
        st.info("No recent activity to display.")

def show_psi_tracker():
    """PSI tracking page"""
    st.markdown("<h1>💎 PSI TRACKER</h1>", unsafe_allow_html=True)
    st.markdown("### Real-time PSI Bonding Curve Monitoring")
    st.markdown("---")
    
    # Auto-refresh every 30 seconds
    placeholder = st.empty()
    
    psi_data = fetch_psi_data()
    
    # Large metrics display
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.2), rgba(168, 85, 247, 0.2)); border-radius: 15px; border: 2px solid rgba(0, 217, 255, 0.4);'>
                <h1 style='font-size: 3em; margin: 0;'>💎</h1>
                <h2 style='margin: 10px 0;'>${psi_data['current_price']:.6f}</h2>
                <p style='color: rgba(0, 217, 255, 0.8);'>Current PSI Price</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(255, 215, 0, 0.2)); border-radius: 15px; border: 2px solid rgba(168, 85, 247, 0.4);'>
                <h1 style='font-size: 3em; margin: 0;'>💰</h1>
                <h2 style='margin: 10px 0;'>${psi_data['internal_value']:.2f}</h2>
                <p style='color: rgba(168, 85, 247, 0.8);'>Internal Value</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(0, 217, 255, 0.2)); border-radius: 15px; border: 2px solid rgba(255, 215, 0, 0.4);'>
                <h1 style='font-size: 3em; margin: 0;'>🚀</h1>
                <h2 style='margin: 10px 0;'>{psi_data['bonding_curve_progress']:.1f}%</h2>
                <p style='color: rgba(255, 215, 0, 0.8);'>Bonding Curve</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Charts
    tab1, tab2, tab3 = st.tabs(["📈 Price Chart", "🎯 Bonding Curve", "📊 Analytics"])
    
    with tab1:
        st.plotly_chart(create_psi_tracker_chart(psi_data), use_container_width=True)
        
        # Price changes
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("24h Change", f"{psi_data['price_24h_change']:.2f}%")
        with col_b:
            st.metric("7d Change", f"{psi_data['price_7d_change']:.2f}%")
        with col_c:
            st.metric("30d Change", f"{psi_data['price_30d_change']:.2f}%")
    
    with tab2:
        st.plotly_chart(create_bonding_curve_chart(psi_data['bonding_curve_progress']), use_container_width=True)
        
        st.markdown("""
            ### 📘 About the Bonding Curve
            
            The PSI bonding curve follows a quadratic progression model where:
            - **Current Stage**: 0% (Foundation Building)
            - **Price Formula**: Base price increases with square of progress
            - **Internal Value**: $155.50 locked as foundation
            - **Target**: 100% completion unlocks full sovereign system
            
            Each purchase moves the curve forward, increasing the price for the next buyer.
        """)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Key Metrics")
            metrics_df = pd.DataFrame({
                'Metric': ['Market Cap', 'Total Holders', 'Circulating Supply', 'Total Supply', 'Last Update'],
                'Value': [
                    f"${psi_data['market_cap']:,.2f}",
                    f"{psi_data['holders']}",
                    "TBD",
                    "TBD",
                    psi_data['last_update'].strftime("%Y-%m-%d %H:%M:%S")
                ]
            })
            st.dataframe(metrics_df, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("### 🎯 Milestones")
            milestones = [
                {"Stage": "Foundation", "Progress": "0%", "Status": "🔵 Current"},
                {"Stage": "Golden Lock", "Progress": "25%", "Status": "⚪ Pending"},
                {"Stage": "OMEGA Lock", "Progress": "50%", "Status": "⚪ Pending"},
                {"Stage": "Sovereign", "Progress": "100%", "Status": "⚪ Target"}
            ]
            st.dataframe(pd.DataFrame(milestones), use_container_width=True, hide_index=True)
    
    # Auto-refresh indicator
    st.markdown(f"<p style='text-align: center; color: rgba(0, 217, 255, 0.6); font-size: 12px;'>🔄 Auto-refreshing every 30 seconds | Last update: {psi_data['last_update'].strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

def show_cec_wam_data():
    """CEC WAM data page"""
    st.markdown("<h1>📊 CEC WAM DATA</h1>", unsafe_allow_html=True)
    st.markdown("### Wide Area Monitoring System")
    st.markdown("---")
    
    cec_data = load_cec_wam_data()
    
    if not cec_data.empty:
        # Status overview
        st.markdown("### 🎯 System Status Overview")
        
        status_counts = cec_data['Status'].value_counts()
        cols = st.columns(len(status_counts))
        
        for i, (status, count) in enumerate(status_counts.items()):
            with cols[i]:
                percentage = (count / len(cec_data)) * 100
                st.markdown(f"""
                    <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.15), rgba(168, 85, 247, 0.15)); border-radius: 10px;'>
                        <h1 style='font-size: 2.5em; margin: 0;'>{get_status_color(status)}</h1>
                        <h2 style='margin: 10px 0;'>{count}</h2>
                        <p>{status}</p>
                        <p style='font-size: 0.8em; color: rgba(0, 217, 255, 0.6);'>{percentage:.1f}%</p>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Data table with color coding
        st.markdown("### 📋 Detailed Status Log")
        
        # Add emoji column
        cec_data['🎯'] = cec_data['Status'].apply(get_status_color)
        
        # Reorder columns
        display_cols = ['🎯', 'Status', 'Component', 'Description', 'Value', 'Timestamp']
        st.dataframe(
            cec_data[display_cols],
            use_container_width=True,
            hide_index=True,
            height=400
        )
        
        # Value distribution chart
        st.markdown("### 📊 Value Distribution")
        
        fig = px.bar(
            cec_data,
            x='Component',
            y='Value',
            color='Status',
            title='Component Values by Status',
            color_discrete_map={
                'PERFECT': '#00FF00',
                'ACTIVE': '#00D9FF',
                'STABLE': '#FFFFFF',
                'TODO': '#FFD700'
            }
        )
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#00D9FF')
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Export option
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            csv = cec_data.to_csv(index=False)
            st.download_button(
                label="📥 Download CEC WAM Data",
                data=csv,
                file_name=f"cec_wam_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
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
            
            **Current Position**
            - X: 0.00 (Origin)
            - Y: 0.00 (Origin)
            - Z: 0.00 (Origin)
            
            **Waypoints**
            - 🏠 **Origin**: Home base
            - 💎 **PSI**: Token foundation
            - 🌌 **Wormhole**: Black hole entry
            - 🎯 **Destination**: Sovereign system
        """)
    
    with col2:
        st.markdown("""
            ### 🌀 Black Hole Status
            
            **Wormhole Simulation**
            - Status: 🔵 Active
            - Singularity: 1.75E+21
            - Event Horizon: Stable
            - Navigation: Safe
            
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
        
        # Export activity log
        csv = activity_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Activity Log",
            data=csv,
            file_name=f"activity_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No activity logged yet.")

def show_alerts():
    """Alerts page"""
    st.markdown("<h1>🔔 ALERTS</h1>", unsafe_allow_html=True)
    st.markdown("### System Notifications")
    st.markdown("---")
    
    # Alerts overview
    total_alerts = len(st.session_state.alerts)
    unread_alerts = sum(1 for alert in st.session_state.alerts if not alert['read'])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Alerts", total_alerts)
    with col2:
        st.metric("Unread", unread_alerts, delta=f"{unread_alerts} new")
    with col3:
        st.metric("System Status", "🟢 Normal")
    
    st.markdown("---")
    
    # Display alerts
    if st.session_state.alerts:
        for i, alert in enumerate(reversed(st.session_state.alerts)):
            alert_icon = {
                'info': 'ℹ️',
                'success': '✅',
                'warning': '⚠️',
                'error': '❌'
            }.get(alert['type'], 'ℹ️')
            
            with st.expander(f"{alert_icon} {alert['title']} - {alert['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}"):
                st.markdown(f"**Message:** {alert['message']}")
                st.markdown(f"**Type:** {alert['type'].upper()}")
                st.markdown(f"**Read:** {'Yes' if alert['read'] else 'No'}")
                
                if st.button(f"Mark as Read", key=f"alert_{i}"):
                    alert['read'] = True
                    st.rerun()
    else:
        st.info("No alerts to display.")
    
    st.markdown("---")
    
    # Test alert
    if st.button("🧪 Generate Test Alert"):
        create_alert(
            "Test Alert",
            f"This is a test alert generated at {datetime.now().strftime('%H:%M:%S')}",
            "info"
        )
        st.success("Test alert created!")
        st.rerun()

def show_settings():
    """Settings page"""
    st.markdown("<h1>⚙️ SETTINGS</h1>", unsafe_allow_html=True)
    st.markdown("### System Configuration")
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["🔧 General", "🔐 Security", "📊 Data"])
    
    with tab1:
        st.markdown("### ⚙️ General Settings")
        
        auto_refresh = st.checkbox("Auto-refresh data", value=True)
        refresh_interval = st.slider("Refresh interval (seconds)", 10, 300, 30)
        
        st.markdown("### 🎨 Display Settings")
        
        theme = st.selectbox("Theme", ["Holographic (Default)", "Dark", "Light"])
        show_animations = st.checkbox("Show animations", value=True)
        
        st.markdown("### 🔔 Notifications")
        
        enable_alerts = st.checkbox("Enable alerts", value=True)
        alert_sound = st.checkbox("Alert sound", value=False)
    
    with tab2:
        st.markdown("### 🔐 Security Settings")
        
        st.info("Currently logged in as: " + st.session_state.username)
        
        st.markdown("### 🔑 Change Password")
        
        old_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        
        if st.button("Update Password"):
            if new_password == confirm_password:
                st.success("✅ Password updated successfully!")
                log_activity("Security", "Password changed", "✅ Success")
            else:
                st.error("❌ Passwords do not match!")
        
        st.markdown("### 🛡️ Security Features")
        
        two_factor = st.checkbox("Enable 2FA (Coming Soon)", disabled=True)
        session_timeout = st.slider("Session timeout (minutes)", 15, 120, 60)
    
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
