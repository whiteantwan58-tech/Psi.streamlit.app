import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Advanced Analytics - Psi Crypto",
    page_icon="📈",
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
        h1 {
            color: #00f5ff;
        }
        h2, h3 {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Data fetching functions
@st.cache_data(ttl=600)  # Cache for 10 minutes
def fetch_historical_data(coin_id, days=30):
    """Fetch historical price data from CoinGecko"""
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart",
            params={
                "vs_currency": "usd",
                "days": days,
                "interval": "daily" if days > 1 else "hourly"
            },
            timeout=15
        )
        response.raise_for_status()
        data = response.json()
        
        # Convert to DataFrame
        prices = data.get('prices', [])
        volumes = data.get('total_volumes', [])
        
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['volume'] = [v[1] for v in volumes]
        
        return df
    except requests.RequestException as e:
        st.error(f"Error fetching data: {str(e)}")
        return get_mock_historical_data(days)

def get_mock_historical_data(days=30):
    """Generate mock historical data for fallback"""
    import numpy as np
    
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    base_price = 50000
    prices = base_price + np.cumsum(np.random.randn(days) * 1000)
    volumes = np.random.uniform(20_000_000_000, 50_000_000_000, days)
    
    df = pd.DataFrame({
        'timestamp': dates,
        'price': prices,
        'volume': volumes
    })
    
    return df

def calculate_moving_averages(df, short_window=7, long_window=30):
    """Calculate moving averages"""
    df['MA_short'] = df['price'].rolling(window=min(short_window, len(df))).mean()
    df['MA_long'] = df['price'].rolling(window=min(long_window, len(df))).mean()
    return df

def create_price_chart(df, coin_name):
    """Create interactive price chart with moving averages"""
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(f'{coin_name} Price', 'Volume'),
        row_heights=[0.7, 0.3]
    )
    
    # Price line
    fig.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['price'],
            name='Price',
            line=dict(color='#00f5ff', width=2)
        ),
        row=1, col=1
    )
    
    # Moving averages if available
    if 'MA_short' in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['MA_short'],
                name='MA 7',
                line=dict(color='#00ff88', width=1, dash='dash')
            ),
            row=1, col=1
        )
    
    if 'MA_long' in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['MA_long'],
                name='MA 30',
                line=dict(color='#ff4444', width=1, dash='dash')
            ),
            row=1, col=1
        )
    
    # Volume bars
    colors = ['#00ff88' if i > 0 and df['price'].iloc[i] >= df['price'].iloc[i-1] 
              else '#ff4444' for i in range(len(df))]
    
    fig.add_trace(
        go.Bar(
            x=df['timestamp'],
            y=df['volume'],
            name='Volume',
            marker_color=colors,
            showlegend=False
        ),
        row=2, col=1
    )
    
    # Update layout
    fig.update_layout(
        template='plotly_dark',
        height=600,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis2_title='Date',
        yaxis_title='Price (USD)',
        yaxis2_title='Volume (USD)',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_candlestick_chart(df, coin_name):
    """Create candlestick chart"""
    # Calculate OHLC from price data
    df['open'] = df['price'].shift(1).fillna(df['price'])
    df['high'] = df[['price', 'open']].max(axis=1) * 1.02
    df['low'] = df[['price', 'open']].min(axis=1) * 0.98
    df['close'] = df['price']
    
    fig = go.Figure(data=[go.Candlestick(
        x=df['timestamp'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='#00ff88',
        decreasing_line_color='#ff4444'
    )])
    
    fig.update_layout(
        title=f'{coin_name} Candlestick Chart',
        template='plotly_dark',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False
    )
    
    return fig

# Header
st.title("📈 Advanced Analytics")
st.markdown("Interactive charts and technical analysis")

# Coin selection
col1, col2 = st.columns([3, 1])

with col1:
    selected_coin = st.selectbox(
        "Select Cryptocurrency",
        options=["Bitcoin", "Ethereum", "Solana"],
        index=0
    )

with col2:
    time_period = st.selectbox(
        "Time Period",
        options=["7 Days", "30 Days", "90 Days"],
        index=1
    )

# Map selections to API values
coin_map = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana"
}

days_map = {
    "7 Days": 7,
    "30 Days": 30,
    "90 Days": 90
}

coin_id = coin_map[selected_coin]
days = days_map[time_period]

# Fetch data
with st.spinner(f"Loading {selected_coin} data..."):
    df = fetch_historical_data(coin_id, days)
    df = calculate_moving_averages(df)

# Display current stats
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

current_price = df['price'].iloc[-1]
price_change = df['price'].iloc[-1] - df['price'].iloc[0]
price_change_pct = (price_change / df['price'].iloc[0]) * 100
high_price = df['price'].max()
low_price = df['price'].min()
avg_volume = df['volume'].mean()

with col1:
    st.metric("Current Price", f"${current_price:,.2f}")

with col2:
    st.metric(
        f"{time_period} Change",
        f"${price_change:,.2f}",
        f"{price_change_pct:.2f}%"
    )

with col3:
    st.metric("Period High", f"${high_price:,.2f}")

with col4:
    st.metric("Period Low", f"${low_price:,.2f}")

# Price chart with moving averages
st.markdown("---")
st.markdown("## 📊 Price Chart with Moving Averages")
price_chart = create_price_chart(df, selected_coin)
st.plotly_chart(price_chart, use_container_width=True)

# Candlestick chart
st.markdown("---")
st.markdown("## 🕯️ Candlestick Chart")
candlestick_chart = create_candlestick_chart(df, selected_coin)
st.plotly_chart(candlestick_chart, use_container_width=True)

# Statistical summary
st.markdown("---")
st.markdown("## 📊 Statistical Summary")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Price Statistics")
    stats_df = pd.DataFrame({
        "Metric": ["Mean", "Median", "Std Dev", "Min", "Max"],
        "Value": [
            f"${df['price'].mean():,.2f}",
            f"${df['price'].median():,.2f}",
            f"${df['price'].std():,.2f}",
            f"${df['price'].min():,.2f}",
            f"${df['price'].max():,.2f}"
        ]
    })
    st.dataframe(stats_df, use_container_width=True, hide_index=True)

with col2:
    st.markdown("### Volume Statistics")
    vol_stats_df = pd.DataFrame({
        "Metric": ["Avg Volume", "Max Volume", "Min Volume"],
        "Value": [
            f"${df['volume'].mean():,.0f}",
            f"${df['volume'].max():,.0f}",
            f"${df['volume'].min():,.0f}"
        ]
    })
    st.dataframe(vol_stats_df, use_container_width=True, hide_index=True)

# Correlation heatmap for multiple coins
st.markdown("---")
st.markdown("## 🔥 Price Correlation Heatmap")

with st.spinner("Calculating correlations..."):
    # Fetch data for all coins
    btc_df = fetch_historical_data('bitcoin', days)
    eth_df = fetch_historical_data('ethereum', days)
    sol_df = fetch_historical_data('solana', days)
    
    # Create correlation matrix
    correlation_data = pd.DataFrame({
        'BTC': btc_df['price'].values[:min(len(btc_df), len(eth_df), len(sol_df))],
        'ETH': eth_df['price'].values[:min(len(btc_df), len(eth_df), len(sol_df))],
        'SOL': sol_df['price'].values[:min(len(btc_df), len(eth_df), len(sol_df))]
    })
    
    corr_matrix = correlation_data.corr()
    
    # Create heatmap
    fig_corr = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdYlGn',
        zmid=0,
        text=corr_matrix.values,
        texttemplate='%{text:.3f}',
        textfont={"size": 16},
        colorbar=dict(title="Correlation")
    ))
    
    fig_corr.update_layout(
        title=f'Price Correlation Matrix ({time_period})',
        template='plotly_dark',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    st.plotly_chart(fig_corr, use_container_width=True)

# Footer
st.markdown("---")
st.caption("💡 Drag to zoom, double-click to reset | Data from CoinGecko API")
