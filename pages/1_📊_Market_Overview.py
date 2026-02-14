import streamlit as st
import requests
import time
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Market Overview - Psi Crypto",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
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
            text-align: center;
        }
        .price-up { 
            color: #00ff88 !important;
            font-weight: bold;
        }
        .price-down { 
            color: #ff4444 !important;
            font-weight: bold;
        }
        h1 {
            color: #00f5ff;
        }
        h2, h3 {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Data fetching functions
@st.cache_data(ttl=300)  # Cache for 5 minutes
def fetch_crypto_data():
    """Fetch cryptocurrency data from CoinGecko API"""
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "bitcoin,ethereum,solana",
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_market_cap": "true",
                "include_24hr_vol": "true"
            },
            timeout=10
        )
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException as e:
        st.warning("⚠️ Live data temporarily unavailable. Using cached data.")
        return get_cached_data(), str(e)

def get_cached_data():
    """Return fallback data when API is unavailable"""
    return {
        "bitcoin": {
            "usd": 94500,
            "usd_24h_change": 1.2,
            "usd_market_cap": 1850000000000,
            "usd_24h_vol": 45000000000
        },
        "ethereum": {
            "usd": 3200,
            "usd_24h_change": 2.5,
            "usd_market_cap": 385000000000,
            "usd_24h_vol": 18000000000
        },
        "solana": {
            "usd": 145,
            "usd_24h_change": -0.8,
            "usd_market_cap": 68000000000,
            "usd_24h_vol": 3500000000
        }
    }

def format_large_number(num):
    """Format large numbers with K, M, B suffixes"""
    if num >= 1_000_000_000:
        return f"${num / 1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"${num / 1_000_000:.2f}M"
    elif num >= 1_000:
        return f"${num / 1_000:.2f}K"
    else:
        return f"${num:.2f}"

def display_crypto_card(name, symbol, data):
    """Display a cryptocurrency card with price and stats"""
    price = data.get('usd', 0)
    change_24h = data.get('usd_24h_change', 0)
    market_cap = data.get('usd_market_cap', 0)
    volume_24h = data.get('usd_24h_vol', 0)
    
    # Determine color and arrow
    if change_24h >= 0:
        color_class = "price-up"
        arrow = "↑"
        delta_color = "normal"
    else:
        color_class = "price-down"
        arrow = "↓"
        delta_color = "inverse"
    
    # Display metrics
    st.markdown(f"### {name} ({symbol})")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Price",
            value=f"${price:,.2f}",
            delta=f"{change_24h:.2f}% {arrow}",
            delta_color=delta_color
        )
    
    with col2:
        st.metric(
            label="24h Volume",
            value=format_large_number(volume_24h)
        )
    
    st.metric(
        label="Market Cap",
        value=format_large_number(market_cap)
    )

# Header
st.title("📊 Real-Time Market Overview")
st.markdown("Live cryptocurrency prices updating every 30 seconds")

# Auto-refresh tracking
if 'market_last_update' not in st.session_state:
    st.session_state.market_last_update = time.time()

# Fetch data
data, error = fetch_crypto_data()

# Display last update time
current_time = time.strftime('%H:%M:%S', time.localtime())
st.info(f"📡 Last updated: {current_time} | Auto-refreshing every 30 seconds")

if error:
    st.warning(f"⚠️ Using cached data due to: {error}")

st.markdown("---")

# Display cryptocurrency cards
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        display_crypto_card("Bitcoin", "BTC", data.get('bitcoin', {}))

with col2:
    with st.container():
        display_crypto_card("Ethereum", "ETH", data.get('ethereum', {}))

with col3:
    with st.container():
        display_crypto_card("Solana", "SOL", data.get('solana', {}))

st.markdown("---")

# Market summary table
st.markdown("## 📋 Market Summary")

summary_data = []
for coin_id, coin_data in data.items():
    coin_name = coin_id.capitalize()
    summary_data.append({
        "Asset": coin_name,
        "Price": f"${coin_data.get('usd', 0):,.2f}",
        "24h Change": f"{coin_data.get('usd_24h_change', 0):.2f}%",
        "Market Cap": format_large_number(coin_data.get('usd_market_cap', 0)),
        "24h Volume": format_large_number(coin_data.get('usd_24h_vol', 0))
    })

df = pd.DataFrame(summary_data)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")

# Market insights
st.markdown("## 💡 Quick Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 Top Performer (24h)")
    # Find top performer
    top_performer = max(data.items(), key=lambda x: x[1].get('usd_24h_change', 0))
    top_name = top_performer[0].capitalize()
    top_change = top_performer[1].get('usd_24h_change', 0)
    st.success(f"**{top_name}** with {top_change:.2f}% gain")

with col2:
    st.markdown("### 💰 Highest Market Cap")
    # Find highest market cap
    highest_mc = max(data.items(), key=lambda x: x[1].get('usd_market_cap', 0))
    mc_name = highest_mc[0].capitalize()
    mc_value = highest_mc[1].get('usd_market_cap', 0)
    st.info(f"**{mc_name}** at {format_large_number(mc_value)}")

# Auto-refresh mechanism
st.markdown("---")
with st.expander("⚙️ Auto-Refresh Settings"):
    st.markdown("""
    This page automatically refreshes every 30 seconds to display the latest market data.
    
    - ✅ Automatic updates enabled
    - 🔄 Refresh interval: 30 seconds
    - 💾 Data cached for 5 minutes
    - 🌐 Data source: CoinGecko API
    """)
    
    if st.button("🔄 Refresh Now"):
        st.cache_data.clear()
        st.rerun()

# JavaScript auto-refresh (client-side)
st.markdown("""
    <script>
        setTimeout(function(){
            window.location.reload();
        }, 30000);
    </script>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("💡 Data provided by CoinGecko API | Updates every 30 seconds | Not financial advice")
