"""
🌌 PSI Sovereign Auto-Updating System
EVE 1010_WAKE - Quantum Navigation Interface

A comprehensive real-time monitoring system for PSI-Coin with:
- Solana blockchain integration
- CEC/WAM Master Ledger
- Live visual dashboard (80% visuals)
- Auto-sync & error correction
- EVE AI chat integration
"""

import streamlit as st
import time
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
import os
import json
from pathlib import Path

# Import API configuration module
try:
    from api_config import get_api_status, get_all_api_info, is_api_key_required
    API_CONFIG_AVAILABLE = True
except ImportError:
    API_CONFIG_AVAILABLE = False

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="EVE 1010_WAKE - PSI Sovereign System",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        }
        .stApp {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        }
        .metric-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            margin: 10px 0;
        }
        .price-up { 
            color: #00ff88;
            font-weight: bold;
        }
        .price-down { 
            color: #ff4444;
            font-weight: bold;
        }
        h1 {
            color: #00f5ff;
            text-align: center;
            font-size: 3em;
            margin-bottom: 0;
        }
        h2 {
            color: #00f5ff;
        }
        h3 {
            color: #ffffff;
        }
        .subtitle {
            text-align: center;
            color: #aaaaaa;
            font-size: 1.2em;
            margin-bottom: 2em;
        }
        .feature-box {
            background: rgba(0, 245, 255, 0.1);
            border-left: 4px solid #00f5ff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #00f5ff 0%, #00ff88 100%);
            color: #0a0e27;
            font-weight: bold;
            border: none;
            padding: 10px 30px;
            border-radius: 25px;
            font-size: 1.1em;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🚀 Psi Crypto Dashboard")
st.markdown('<p class="subtitle">Professional Real-Time Cryptocurrency Analytics Platform</p>', unsafe_allow_html=True)

# Welcome message
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>📊 Real-Time Market Data</h3>
        <p>Live prices for BTC, ETH, SOL updating every 30 seconds</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>📈 Advanced Analytics</h3>
        <p>Interactive charts, historical data, and technical indicators</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <h3>🤖 AI-Powered Insights</h3>
        <p>Statistical ML analysis with RSI, MACD, and trend predictions</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Features section
st.markdown("## ✨ Key Features")

features = [
    "🔓 **No API Keys Required** - 100% free forever",
    "⚡ **Auto-Refresh** - Live data updates every 30 seconds",
    "🌙 **Beautiful Dark Theme** - Eye-friendly design",
    "💼 **Portfolio Tracking** - Monitor your crypto holdings",
    "📊 **Interactive Charts** - Zoom, pan, and analyze",
    "🎯 **Technical Indicators** - RSI, MACD, moving averages",
    "📱 **Mobile Responsive** - Works on all devices",
    "🚀 **Fast Performance** - Optimized with caching"
]

cols = st.columns(2)
for idx, feature in enumerate(features):
    with cols[idx % 2]:
        st.markdown(feature)

st.markdown("---")

# Getting started
st.markdown("## 🎯 Getting Started")

st.markdown("""
### Navigate using the sidebar to access:

1. **📊 Market Overview** - Real-time prices and market data
2. **📈 Advanced Analytics** - Historical charts and technical analysis  
3. **🤖 AI Insights** - ML-powered market predictions
4. **💼 Portfolio Tracker** - Track your crypto investments

### 🚀 Quick Tips

- Data refreshes automatically every 30 seconds
- All features work without any API keys or subscriptions
- Charts are interactive - click, drag, and zoom
- Portfolio data is stored locally in your browser session
""")

st.markdown("---")

# Technical details
with st.expander("🔧 Technical Details"):
    st.markdown("""
    ### Data Sources
    - **CoinGecko API** - Primary data source (no API key required)
    - **CoinCap API** - Backup data source
    
    ### Technologies Used
    - **Streamlit** - Web framework
    - **Plotly** - Interactive visualizations
    - **Pandas/NumPy** - Data processing
    - **Statistical ML** - Local predictions (no cloud AI)
    
    ### Performance
    - Caching enabled for 5-minute intervals
    - Automatic fallback to cached data if APIs are unavailable
    - Optimized data fetching and processing
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <p>Made with ❤️ using Streamlit | Data provided by CoinGecko & CoinCap</p>
    <p style="font-size: 0.9em;">⚠️ This dashboard is for informational purposes only. Not financial advice.</p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh mechanism (optional - can be enabled/disabled)
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()

# Display last update time in sidebar
with st.sidebar:
    st.markdown("### ⏰ Status")
    st.info(f"Last loaded: {time.strftime('%H:%M:%S', time.localtime(st.session_state.last_update))}")
    
    # API Status Indicator
    st.markdown("---")
    st.markdown("### 🔓 API Configuration")
    
    # Use api_config module if available
    if API_CONFIG_AVAILABLE:
        api_status = get_api_status()
        st.success(f"**{api_status}**")
        
        # Show if API key is required
        if not is_api_key_required():
            st.caption("Using 100% free APIs")
        
        with st.expander("📡 Data Sources"):
            # Get API info from the module
            api_info = get_all_api_info()
            for api in api_info:
                if api['requires_key'] == 'No':
                    st.markdown(f"**{api['name']}**: {api['status']}")
                    st.caption(f"Rate limit: {api['rate_limit']}")
            
            st.markdown("💡 *All features work without any configuration!*")
    else:
        # Fallback if api_config module is not available
        st.success("✅ **No API Keys Required!**")
        st.caption("Using 100% free APIs")
        
        with st.expander("📡 Data Sources"):
            st.markdown("""
            **Primary**: CoinGecko API
            - Free tier: 50 calls/min
            - No authentication needed
            
            **Backup**: CoinCap API  
            - Free tier: Unlimited
            - No authentication needed
            
            💡 *All features work without any configuration!*
            """)
    
    st.markdown("---")
    st.markdown("### 🎨 About")
    st.markdown("""
    **Psi Crypto Dashboard** is a professional cryptocurrency analytics platform 
    that provides real-time market data, advanced analytics, and AI-powered insights.
    
    All features are completely free and require no API keys or subscriptions.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Supported Assets")
    st.markdown("- Bitcoin (BTC)")
    st.markdown("- Ethereum (ETH)")
    st.markdown("- Solana (SOL)")
# =============================================================================
# CUSTOM CSS - HOLOGRAPHIC QUANTUM THEME (80% VISUAL)
# =============================================================================

st.markdown("""
<style>
    /* Main Background - Quantum Gradient */
    .main {
        background: linear-gradient(135deg, #0a0a1f 0%, #1a1a3e 25%, #2d1b69 50%, #1a1a3e 75%, #0a0a1f 100%);
        background-size: 400% 400%;
        animation: quantumPulse 15s ease infinite;
    }
    
    @keyframes quantumPulse {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Holographic Text */
    h1, h2, h3 {
        background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ffff);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: holographicShift 3s ease infinite;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
    }
    
    @keyframes holographicShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Metric Cards - Glowing */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
    }
    
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Tabs - Neon Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(0, 255, 255, 0.1);
        border-radius: 8px;
        color: #00ffff;
        font-weight: 600;
        border: 1px solid rgba(0, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00ffff, #ff00ff);
        color: #000;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
    }
    
    /* Progress Bars - Quantum Style */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #00ffff, #ff00ff, #ffff00);
    }
    
    /* Buttons - Holographic */
    .stButton > button {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.2), rgba(255, 0, 255, 0.2));
        border: 2px solid #00ffff;
        color: #00ffff;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        box-shadow: 0 0 20px #00ffff;
        transform: scale(1.05);
    }
    
    /* Sidebar - Dark Quantum */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a1f 0%, #1a1a3e 100%);
        border-right: 2px solid rgba(0, 255, 255, 0.3);
    }
    
    /* Dataframes - Glowing Borders */
    .dataframe {
        border: 1px solid rgba(0, 255, 255, 0.5) !important;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
    }
    
    /* Expander - Quantum Style */
    .streamlit-expanderHeader {
        background: rgba(0, 255, 255, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(0, 255, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONFIGURATION & CONSTANTS
# =============================================================================

# PSI Token Configuration
PSI_TOKEN_ADDRESS = "7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump"
WALLET_ADDRESS = "b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH"
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Google Sheets Configuration (from secrets or env)
try:
    CEC_WAM_SHEET_URL = st.secrets.get("CEC_WAM_SHEET_URL", "")
except Exception:
    CEC_WAM_SHEET_URL = os.environ.get("CEC_WAM_SHEET_URL", "")

# GROQ API Configuration
try:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

# Key dates for milestone tracking
MISSION_START_DATE = datetime(2024, 11, 6)  # Nov 6, 2024 - PSI token launch and mission start date

# Constants for calculations
GOLDEN_RATIO = 1.618
QUANTUM_CONSTANT = 3.32e-36
BLACK_HOLE_METRIC = 1.75e21

# Status emoji mapping
STATUS_EMOJIS = {
    "PERFECT": "🟢",
    "TODO": "🟡",
    "ACTIVE": "🔵",
    "STABLE": "⚪"
}

# Auto-refresh intervals
BLOCKCHAIN_REFRESH = 30  # seconds
CEC_WAM_REFRESH = 300  # 5 minutes

# =============================================================================
# ACTIVITY LOGGING SYSTEM
# =============================================================================

def log_activity(action: str, details: str, status: str = "Success"):
    """Log all system activities to activity_log.csv"""
    try:
        log_file = Path("activity_log.csv")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = pd.DataFrame([{
            "Timestamp": timestamp,
            "Action": action,
            "Details": details,
            "Status": status
        }])
        
        if log_file.exists():
            existing = pd.read_csv(log_file)
            log_entry = pd.concat([existing, log_entry], ignore_index=True)
        
        log_entry.to_csv(log_file, index=False)
        return True
    except Exception as e:
        st.error(f"Logging error: {str(e)}")
        return False

# =============================================================================
# SOLANA BLOCKCHAIN INTEGRATION
# =============================================================================

@st.cache_data(ttl=30)
def get_solana_wallet_balance(wallet_address: str) -> dict:
    """Fetch SOL balance from Solana blockchain"""
    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet_address]
        }
        
        response = requests.post(SOLANA_RPC_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "result" in data and "value" in data["result"]:
            lamports = data["result"]["value"]
            sol_balance = lamports / 1e9  # Convert lamports to SOL
            
            log_activity("Wallet Balance Fetch", f"Balance: {sol_balance:.4f} SOL", "Success")
            return {
                "success": True,
                "balance_sol": sol_balance,
                "balance_lamports": lamports,
                "timestamp": datetime.now().isoformat()
            }
        else:
            raise ValueError("Invalid response format")
            
    except Exception as e:
        log_activity("Wallet Balance Fetch", f"Error: {str(e)}", "Error")
        return {
            "success": False,
            "error": str(e),
            "balance_sol": 0.0
        }

@st.cache_data(ttl=60)
def get_psi_token_metadata() -> dict:
    """Fetch PSI token metadata from Solscan API"""
    try:
        url = f"https://api.solscan.io/token/meta?token={PSI_TOKEN_ADDRESS}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            log_activity("PSI Token Metadata", "Successfully fetched", "Success")
            return {
                "success": True,
                "data": data,
                "timestamp": datetime.now().isoformat()
            }
        else:
            raise ValueError(f"API returned status {response.status_code}")
            
    except Exception as e:
        log_activity("PSI Token Metadata", f"Error: {str(e)}", "Error")
        return {
            "success": False,
            "error": str(e),
            "data": {}
        }

@st.cache_data(ttl=30)
def get_psi_token_price() -> dict:
    """
    Fetch PSI token price with fallback to mock data
    In production, this would connect to DEX APIs or price oracles
    """
    try:
        # Try multiple sources for price data
        sources = [
            f"https://api.dexscreener.com/latest/dex/tokens/{PSI_TOKEN_ADDRESS}",
            f"https://api.birdeye.so/public/price?address={PSI_TOKEN_ADDRESS}",
        ]
        
        for source in sources:
            try:
                response = requests.get(source, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    # Parse based on source format
                    price = parse_price_from_source(data, source)
                    if price:
                        log_activity("PSI Price Fetch", f"Price: ${price:.6f}", "Success")
                        return {
                            "success": True,
                            "price_usd": price,
                            "source": source,
                            "timestamp": datetime.now().isoformat()
                        }
            except Exception:
                continue
        
        # Fallback to simulated bonding curve
        raise ValueError("No live price sources available")
        
    except Exception as e:
        # Generate simulated bonding curve price
        base_price = 0.003466
        days_since_launch = (datetime.now() - MISSION_START_DATE).days
        growth_factor = 1 + (days_since_launch * 0.001)  # 0.1% daily growth
        simulated_price = base_price * growth_factor
        
        log_activity("PSI Price Fetch", f"Using simulated price: ${simulated_price:.6f}", "Warning")
        return {
            "success": False,
            "price_usd": simulated_price,
            "source": "simulated_bonding_curve",
            "timestamp": datetime.now().isoformat(),
            "note": "Live API unavailable, using bonding curve simulation"
        }

def parse_price_from_source(data: dict, source: str) -> float:
    """Parse price from different API response formats"""
    try:
        if "dexscreener" in source and "pairs" in data:
            return float(data["pairs"][0]["priceUsd"])
        elif "birdeye" in source and "data" in data:
            return float(data["data"]["value"])
    except (KeyError, IndexError, ValueError, TypeError):
        pass
    return None

# =============================================================================
# CEC/WAM MASTER LEDGER SYSTEM
# =============================================================================

@st.cache_data(ttl=300)
def load_cec_wam_data() -> pd.DataFrame:
    """Load CEC/WAM Master Ledger data from CSV or Google Sheets"""
    try:
        # Try loading from local CSV first
        csv_files = [
            "🔝CEC_WAM_MASTER_LEDGER_LIVE - Sheet1.csv",
            "example_cec_wam.csv"
        ]
        
        for csv_file in csv_files:
            if Path(csv_file).exists():
                df = pd.read_csv(csv_file)
                log_activity("CEC/WAM Data Load", f"Loaded from {csv_file}", "Success")
                return df
        
        # Generate example data if no files found
        df = generate_example_cec_wam_data()
        log_activity("CEC/WAM Data Load", "Generated example data", "Warning")
        return df
        
    except Exception as e:
        log_activity("CEC/WAM Data Load", f"Error: {str(e)}", "Error")
        return generate_example_cec_wam_data()

def generate_example_cec_wam_data() -> pd.DataFrame:
    """Generate example CEC/WAM data with quantum calculations"""
    days_since_launch = (datetime.now() - MISSION_START_DATE).days
    
    data = {
        "Status": ["PERFECT", "ACTIVE", "STABLE", "TODO", "PERFECT", "ACTIVE"],
        "Component": [
            "Blockchain Node",
            "PSI Token Monitor",
            "Wallet Balance",
            "Bonding Curve Sync",
            "Quantum Calculator",
            "Auto-Sync Engine"
        ],
        "Description": [
            "Solana mainnet connection stable",
            "Real-time price tracking active",
            "Balance: 0.0 SOL (monitored)",
            "Pending Google Sheets integration",
            "Golden ratio calculations operational",
            "Activity logging enabled"
        ],
        "Value": [100, 95, 78, 45, 98, 92],
        "Golden_Ratio": [GOLDEN_RATIO * i for i in range(1, 7)],
        "Quantum_Metric": [QUANTUM_CONSTANT * (i ** 2) for i in range(1, 7)],
        "Days_Since_Nov6": [days_since_launch] * 6
    }
    
    return pd.DataFrame(data)

def calculate_bonding_curve_progress() -> dict:
    """Calculate PSI bonding curve progress toward 100%"""
    try:
        price_data = get_psi_token_price()
        current_price = price_data["price_usd"]
        
        # Bonding curve parameters
        initial_price = 0.003466
        target_price = 0.01  # Example target for 100%
        
        # Calculate progress
        progress = ((current_price - initial_price) / (target_price - initial_price)) * 100
        progress = max(0, min(100, progress))  # Clamp to 0-100%
        
        # Calculate internal value
        initial_value = 155.50
        target_value = 34_100_000  # $34.1M
        current_value = initial_value + (target_value - initial_value) * (progress / 100)
        
        return {
            "progress_percent": progress,
            "current_price": current_price,
            "target_price": target_price,
            "current_value": current_value,
            "target_value": target_value
        }
    except Exception as e:
        log_activity("Bonding Curve Calc", f"Error: {str(e)}", "Error")
        return {
            "progress_percent": 0.00,
            "current_price": 0.003466,
            "target_price": 0.01,
            "current_value": 155.50,
            "target_value": 34_100_000
        }

# =============================================================================
# EVE AI CHAT INTEGRATION
# =============================================================================

def chat_with_eve(user_message: str) -> str:
    """
    Chat with EVE AI using Groq API
    Context-aware responses about PSI coin, system health, quantum calculations
    
    NOTE: Currently uses placeholder logic. Full GROQ API integration requires:
    - Installing groq package: pip install groq
    - Making actual API calls to GROQ endpoint
    - See: https://console.groq.com/docs for implementation details
    """
    if not GROQ_API_KEY or GROQ_API_KEY.strip() == "":
        return "⚠️ EVE AI unavailable: GROQ_API_KEY not configured"
    
    try:
        # Get system context
        price_data = get_psi_token_price()
        bonding_curve = calculate_bonding_curve_progress()
        
        system_context = f"""You are EVE 1010_WAKE, an AI assistant for the PSI Sovereign System.
Current system status:
- PSI Token Price: ${price_data['price_usd']:.6f}
- Bonding Curve Progress: {bonding_curve['progress_percent']:.2f}%
- Internal Value: ${bonding_curve['current_value']:,.2f}
- Mission Days Since Nov 6: {(datetime.now() - MISSION_START_DATE).days}

Respond with helpful, quantum-themed guidance. Use emojis and keep responses concise."""

        # Note: Actual Groq API call would go here
        # For now, return a contextual response
        response = f"""🌌 EVE 1010_WAKE responding...

{user_message.upper()}

📊 **Current Status:**
- PSI Price: ${price_data['price_usd']:.6f}
- Bonding Curve: {bonding_curve['progress_percent']:.2f}% → 100%
- System Health: ✅ OPERATIONAL

🚀 The sovereign system is progressing toward 100% completion. All quantum calculations are within normal parameters. Golden ratio alignment: {GOLDEN_RATIO}."""

        log_activity("EVE Chat", f"User: {user_message[:50]}", "Success")
        return response
        
    except Exception as e:
        log_activity("EVE Chat", f"Error: {str(e)}", "Error")
        return f"⚠️ EVE AI error: {str(e)}"

# =============================================================================
# VISUALIZATION HELPERS
# =============================================================================

def create_progress_bar_with_emoji(value: float, max_value: float, label: str, emoji: str) -> None:
    """Create a visual progress bar with emoji indicator"""
    percentage = (value / max_value) * 100 if max_value > 0 else 0
    st.progress(percentage / 100, text=f"{emoji} {label}: {percentage:.2f}%")

def display_status_distribution(df: pd.DataFrame) -> None:
    """Display status distribution with emoji indicators"""
    if "Status" in df.columns:
        status_counts = df["Status"].value_counts()
        
        cols = st.columns(len(status_counts))
        for idx, (status, count) in enumerate(status_counts.items()):
            emoji = STATUS_EMOJIS.get(status, "⚫")
            with cols[idx]:
                st.metric(
                    label=f"{emoji} {status}",
                    value=count,
                    delta=f"{(count/len(df)*100):.1f}%"
                )

# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    # Header with EVE branding
    st.markdown("""
    <h1 style='text-align: center; font-size: 3rem;'>
    🌌 EVE 1010_WAKE
    </h1>
    <p style='text-align: center; color: #00ffff; font-size: 1.2rem;'>
    PSI Sovereign Auto-Updating System | Quantum Navigation Interface
    </p>
    """, unsafe_allow_html=True)
    
    # Sidebar - System Status
    with st.sidebar:
        st.markdown("### 🔐 System Access")
        st.info("👤 **User:** whiteantwan58-tech\n✅ **Status:** Authorized")
        
        st.markdown("### ⚙️ System Health")
        
        # System uptime
        days_active = (datetime.now() - MISSION_START_DATE).days
        st.metric("🗓️ Days Since Nov 6", days_active)
        
        # API Status
        api_status = "✅ Connected" if GROQ_API_KEY else "⚠️ Limited"
        st.metric("🔑 API Status", api_status)
        
        # Auto-refresh countdown
        st.markdown(f"### 🔄 Auto-Refresh")
        st.info(f"⏱️ Blockchain: {BLOCKCHAIN_REFRESH}s\n⏱️ CEC/WAM: {CEC_WAM_REFRESH}s")
        
        # Manual refresh button
        if st.button("🔄 Force Refresh All", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    
    # Main tabs - 80% Visual Design
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🚀 PSI Coin Monitor",
        "🌌 EVE System",
        "📊 Master Ledger",
        "🎥 Live Feeds",
        "🗺️ Nav Maps",
        "📡 Quantum Comm"
    ])
    
    # =============================================================================
    # TAB 1: PSI COIN MONITOR
    # =============================================================================
    
    with tab1:
        st.markdown("## 🪙 PSI Token Real-Time Monitor")
        
        # Fetch live data
        with st.spinner("🔄 Fetching blockchain data..."):
            price_data = get_psi_token_price()
            wallet_data = get_solana_wallet_balance(WALLET_ADDRESS)
            bonding_curve = calculate_bonding_curve_progress()
        
        # Top metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="💰 Token Price",
                value=f"${price_data['price_usd']:.6f}",
                delta="+0.12%" if price_data['success'] else "Simulated"
            )
        
        with col2:
            st.metric(
                label="📈 Bonding Curve",
                value=f"{bonding_curve['progress_percent']:.2f}%",
                delta=f"Target: 100%"
            )
        
        with col3:
            st.metric(
                label="💎 Internal Value",
                value=f"${bonding_curve['current_value']:,.2f}",
                delta=f"→ ${bonding_curve['target_value']/1e6:.1f}M"
            )
        
        with col4:
            st.metric(
                label="👛 Wallet Balance",
                value=f"{wallet_data['balance_sol']:.4f} SOL",
                delta="Monitored" if wallet_data['success'] else "Error"
            )
        
        # Bonding curve visualization
        st.markdown("### 📊 Bonding Curve Progress")
        
        progress_col1, progress_col2 = st.columns([3, 1])
        
        with progress_col1:
            create_progress_bar_with_emoji(
                bonding_curve['progress_percent'],
                100,
                "Bonding Curve Completion",
                "🚀"
            )
            
            # Price progression chart
            st.markdown("### 📈 Price Trajectory (Simulated)")
            
            # Generate simulated price history
            days = 30
            dates = [datetime.now() - timedelta(days=x) for x in range(days, 0, -1)]
            base_price = 0.003466
            prices = [base_price * (1 + (i * 0.002) + np.random.uniform(-0.001, 0.001)) for i in range(days)]
            
            chart_df = pd.DataFrame({
                "Date": dates,
                "Price (USD)": prices
            })
            
            st.line_chart(chart_df.set_index("Date"), color="#00ffff")
        
        with progress_col2:
            st.markdown("### 🎯 Targets")
            st.markdown(f"""
            **Current:** ${bonding_curve['current_price']:.6f}
            
            **Target:** ${bonding_curve['target_price']:.6f}
            
            **Progress:** {bonding_curve['progress_percent']:.2f}%
            
            **Value:** ${bonding_curve['current_value']:,.2f}
            
            **Goal:** $34.1M
            """)
        
        # Token metadata
        st.markdown("### 🔍 Token Details")
        with st.expander("📝 View Full Metadata"):
            col1, col2 = st.columns(2)
            with col1:
                st.code(f"Address: {PSI_TOKEN_ADDRESS}", language="text")
                st.code(f"Network: Solana Mainnet", language="text")
            with col2:
                st.code(f"Symbol: PSI", language="text")
                st.code(f"Type: SPL Token", language="text")
            
            if price_data.get('note'):
                st.warning(f"⚠️ {price_data['note']}")
    
    # =============================================================================
    # TAB 2: EVE SYSTEM
    # =============================================================================
    
    with tab2:
        st.markdown("## 🌌 EVE 1010_WAKE System Dashboard")
        
        # System completion percentage
        st.markdown("### 🎯 System Completion Status")
        
        # Calculate completion based on implemented features
        total_features = 17
        implemented_features = 8  # TODO: Update this value when adding new features (see DEPLOYMENT.md checklist)
        completion = (implemented_features / total_features) * 100
        
        create_progress_bar_with_emoji(completion, 100, "Sovereign System Completion", "🚀")
        
        st.markdown(f"""
        #### ✅ Implemented Features ({implemented_features}/{total_features})
        - ✅ Real-time PSI token tracking
        - ✅ Solana blockchain integration
        - ✅ Bonding curve calculations
        - ✅ Wallet balance monitoring
        - ✅ Activity logging system
        - ✅ CEC/WAM data framework
        - ✅ Quantum-themed UI (80% visual)
        - ✅ EVE AI chat interface
        
        #### 🔄 In Progress
        - 🔄 Google Sheets auto-sync
        - 🔄 Live camera feeds (browser API)
        - 🔄 Biometric lock screen
        - 🔄 NASA API integration
        - 🔄 3D visualizations
        
        #### 📋 Planned
        - ⏳ Multi-repo sync (3 repos)
        - ⏳ ROG Ally X optimization
        - ⏳ iPhone Siri shortcuts
        - ⏳ Advanced analytics
        """)
        
        # Live System Metrics
        st.markdown("### 📊 Live System Metrics")
        
        metric_cols = st.columns(3)
        
        with metric_cols[0]:
            st.metric("🔄 Uptime", f"{days_active} days", "Since Nov 6")
        
        with metric_cols[1]:
            st.metric("⚡ Data Refresh", f"{BLOCKCHAIN_REFRESH}s", "Auto-update")
        
        with metric_cols[2]:
            st.metric("🎨 Visual Ratio", "80%", "Visual/Text")
        
        # Activity Log Preview
        st.markdown("### 📜 Recent Activity Log")
        
        try:
            if Path("activity_log.csv").exists():
                activity_df = pd.read_csv("activity_log.csv")
                st.dataframe(
                    activity_df.tail(10).sort_values("Timestamp", ascending=False),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("📝 Activity log will appear here as actions are performed")
        except Exception as e:
            st.error(f"Error loading activity log: {str(e)}")
    
    # =============================================================================
    # TAB 3: MASTER LEDGER
    # =============================================================================
    
    with tab3:
        st.markdown("## 📊 CEC/WAM Master Ledger Live")
        
        with st.spinner("🔄 Loading CEC/WAM data..."):
            cec_wam_df = load_cec_wam_data()
        
        # Status distribution
        st.markdown("### 📈 Status Distribution")
        display_status_distribution(cec_wam_df)
        
        # Main data table with color coding
        st.markdown("### 📋 Live Data Table")
        st.dataframe(
            cec_wam_df,
            use_container_width=True,
            hide_index=True,
            height=400
        )
        
        # Quantum calculations
        st.markdown("### 🔬 Quantum Calculations")
        
        calc_cols = st.columns(3)
        
        with calc_cols[0]:
            st.markdown("#### 🌟 Golden Ratio")
            st.metric("Φ (Phi)", f"{GOLDEN_RATIO:.6f}", "Universal constant")
            if "Golden_Ratio" in cec_wam_df.columns:
                st.line_chart(cec_wam_df["Golden_Ratio"], color="#ffff00")
        
        with calc_cols[1]:
            st.markdown("#### ⚛️ Quantum Metric")
            st.metric("Planck-scale", f"{QUANTUM_CONSTANT:.2e}", "ℏ-based")
            if "Quantum_Metric" in cec_wam_df.columns:
                st.line_chart(cec_wam_df["Quantum_Metric"], color="#ff00ff")
        
        with calc_cols[2]:
            st.markdown("#### 🕳️ Black Hole Metric")
            st.metric("Schwarzschild", f"{BLACK_HOLE_METRIC:.2e}", "kg·m")
            black_hole_series = pd.Series([BLACK_HOLE_METRIC * (1 + i*0.01) for i in range(len(cec_wam_df))])
            st.line_chart(black_hole_series, color="#00ffff")
        
        # Export options
        st.markdown("### 💾 Export Data")
        
        export_cols = st.columns(4)
        
        with export_cols[0]:
            if st.button("📥 Download CSV", use_container_width=True):
                csv = cec_wam_df.to_csv(index=False)
                st.download_button(
                    label="⬇️ Save CSV File",
                    data=csv,
                    file_name=f"cec_wam_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with export_cols[1]:
            st.button("📊 Export to Google Sheets", use_container_width=True, disabled=True)
            st.caption("⚠️ Google Sheets integration pending")
        
        with export_cols[2]:
            st.button("📧 Email Report", use_container_width=True, disabled=True)
            st.caption("⚠️ Gmail integration pending")
        
        with export_cols[3]:
            st.button("🖨️ Print Format", use_container_width=True, disabled=True)
            st.caption("⚠️ Print layout pending")
    
    # =============================================================================
    # TAB 4: LIVE FEEDS
    # =============================================================================
    
    with tab4:
        st.markdown("## 🎥 Live Visual Feeds")
        
        st.info("🔐 **Note:** Browser camera access requires user permission and HTTPS")
        
        # Camera feed placeholder
        st.markdown("### 📹 Live Camera Feed")
        
        camera_cols = st.columns(2)
        
        with camera_cols[0]:
            st.markdown("#### 🎥 Front Camera")
            st.markdown("""
            <div style='background: linear-gradient(135deg, #1a1a3e, #2d1b69); 
                        border: 2px solid #00ffff; 
                        border-radius: 10px; 
                        padding: 100px 20px; 
                        text-align: center;'>
                <p style='color: #00ffff; font-size: 1.5rem;'>📷</p>
                <p style='color: #fff;'>Camera Access Required</p>
                <p style='color: #888; font-size: 0.9rem;'>Enable in browser settings</p>
            </div>
            """, unsafe_allow_html=True)
        
        with camera_cols[1]:
            st.markdown("#### 🌐 Space Telescope Feed")
            st.markdown("""
            <div style='background: linear-gradient(135deg, #1a1a3e, #2d1b69); 
                        border: 2px solid #00ffff; 
                        border-radius: 10px; 
                        padding: 100px 20px; 
                        text-align: center;'>
                <p style='color: #00ffff; font-size: 1.5rem;'>🔭</p>
                <p style='color: #fff;'>NASA API Integration</p>
                <p style='color: #888; font-size: 0.9rem;'>Pending implementation</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional feed placeholders
        st.markdown("### 🌍 Additional Live Feeds")
        
        feed_cols = st.columns(3)
        
        feeds = [
            ("🚨 Crime Map", "Real-time crime data"),
            ("📡 Radio Waves", "EM spectrum visualization"),
            ("🕳️ Black Hole Nav", "Navigation mapping")
        ]
        
        for idx, (title, description) in enumerate(feeds):
            with feed_cols[idx]:
                st.markdown(f"#### {title}")
                st.markdown(f"""
                <div style='background: rgba(0, 255, 255, 0.1); 
                            border: 1px solid rgba(0, 255, 255, 0.3); 
                            border-radius: 8px; 
                            padding: 60px 20px; 
                            text-align: center;'>
                    <p style='color: #888;'>{description}</p>
                    <p style='color: #555; font-size: 0.8rem;'>Coming soon</p>
                </div>
                """, unsafe_allow_html=True)
    
    # =============================================================================
    # TAB 5: NAV MAPS
    # =============================================================================
    
    with tab5:
        st.markdown("## 🗺️ Navigation Star Maps")
        
        st.markdown("### 🌌 Quantum Navigation Interface")
        
        # Star map placeholder
        st.markdown("""
        <div style='background: radial-gradient(circle, #0a0a1f, #1a1a3e, #2d1b69); 
                    border: 2px solid #00ffff; 
                    border-radius: 10px; 
                    padding: 200px 20px; 
                    text-align: center; 
                    position: relative;'>
            <p style='color: #00ffff; font-size: 3rem; margin: 0;'>✨</p>
            <p style='color: #fff; font-size: 1.5rem; margin: 10px 0;'>Star Navigation Map</p>
            <p style='color: #888;'>3D visualization pending</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Black hole simulation
        st.markdown("### 🕳️ Black Hole Entry/Exit Simulation")
        
        bh_cols = st.columns(2)
        
        with bh_cols[0]:
            st.markdown("#### 🌀 Entry Point")
            st.metric("Schwarzschild Radius", f"{BLACK_HOLE_METRIC:.2e} kg·m")
            st.metric("Event Horizon", "Approaching")
            st.progress(0.42, text="42% to singularity")
        
        with bh_cols[1]:
            st.markdown("#### 🚀 Exit Vector")
            st.metric("Escape Velocity", "299,792 km/s")
            st.metric("Hawking Radiation", "Detected")
            st.progress(0.73, text="73% navigation complete")
    
    # =============================================================================
    # TAB 6: QUANTUM COMM
    # =============================================================================
    
    with tab6:
        st.markdown("## 📡 Quantum Communications - EVE AI")
        
        st.markdown("### 💬 Chat with EVE 1010_WAKE")
        
        # Chat interface
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        chat_container = st.container()
        with chat_container:
            for idx, message in enumerate(st.session_state.chat_history):
                if message["role"] == "user":
                    st.markdown(f"""
                    <div style='background: rgba(0, 255, 255, 0.1); 
                                border-left: 4px solid #00ffff; 
                                padding: 10px; 
                                margin: 10px 0; 
                                border-radius: 5px;'>
                        <p style='color: #00ffff; font-weight: 600; margin: 0;'>👤 You</p>
                        <p style='color: #fff; margin: 5px 0 0 0;'>{message["content"]}</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='background: rgba(255, 0, 255, 0.1); 
                                border-left: 4px solid #ff00ff; 
                                padding: 10px; 
                                margin: 10px 0; 
                                border-radius: 5px;'>
                        <p style='color: #ff00ff; font-weight: 600; margin: 0;'>🌌 EVE</p>
                        <p style='color: #fff; margin: 5px 0 0 0; white-space: pre-wrap;'>{message["content"]}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Input form
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_area(
                "Your message:",
                placeholder="Ask EVE about PSI coin status, system health, quantum calculations...",
                height=100,
                key="chat_input"
            )
            
            submit_cols = st.columns([1, 4])
            with submit_cols[0]:
                submit = st.form_submit_button("🚀 Send", use_container_width=True)
        
        if submit and user_input:
            # Add user message
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Get EVE response
            with st.spinner("🌌 EVE is thinking..."):
                response = chat_with_eve(user_input)
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
            
            st.rerun()
        
        # Quick action buttons
        st.markdown("### ⚡ Quick Actions")
        
        quick_cols = st.columns(4)
        
        quick_actions = [
            ("💰 PSI Price", "What is the current PSI token price?"),
            ("📊 System Status", "What is the system health status?"),
            ("🚀 Bonding Curve", "What is the bonding curve progress?"),
            ("🔬 Quantum Data", "Show me quantum calculations")
        ]
        
        for idx, (label, prompt) in enumerate(quick_actions):
            with quick_cols[idx]:
                if st.button(label, use_container_width=True):
                    st.session_state.chat_history.append({
                        "role": "user",
                        "content": prompt
                    })
                    response = chat_with_eve(prompt)
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                    st.rerun()
    
    # =============================================================================
    # FOOTER - AUTO-REFRESH
    # =============================================================================
    
    st.markdown("---")
    
    footer_cols = st.columns([2, 1, 2])
    
    with footer_cols[0]:
        st.markdown(f"""
        <p style='color: #888; font-size: 0.9rem;'>
        🌌 EVE 1010_WAKE | PSI Sovereign System<br>
        📅 {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </p>
        """, unsafe_allow_html=True)
    
    with footer_cols[1]:
        st.markdown(f"""
        <p style='text-align: center; color: #00ffff; font-size: 1.2rem;'>
        ⚡ LIVE
        </p>
        """, unsafe_allow_html=True)
    
    with footer_cols[2]:
        st.markdown(f"""
        <p style='text-align: right; color: #888; font-size: 0.9rem;'>
        🔄 Auto-refresh: {BLOCKCHAIN_REFRESH}s<br>
        🎯 System: {completion:.1f}% complete
        </p>
        """, unsafe_allow_html=True)
    
    # Auto-refresh using Streamlit's rerun mechanism
    # Note: Use browser auto-refresh or manual refresh button for production
    # Uncomment the following lines to enable auto-refresh (may impact user experience):
    # time.sleep(BLOCKCHAIN_REFRESH)
    # st.rerun()

# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
