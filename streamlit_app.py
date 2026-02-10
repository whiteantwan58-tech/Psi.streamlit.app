import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Psi Crypto Dashboard",
    page_icon="🚀",
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
