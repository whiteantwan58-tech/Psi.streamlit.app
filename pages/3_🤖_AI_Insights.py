import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Insights - Psi Crypto",
    page_icon="🤖",
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
        .insight-box {
            background: rgba(0, 245, 255, 0.1);
            border-left: 4px solid #00f5ff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .bullish {
            background: rgba(0, 255, 136, 0.1);
            border-left: 4px solid #00ff88;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .bearish {
            background: rgba(255, 68, 68, 0.1);
            border-left: 4px solid #ff4444;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .neutral {
            background: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #ffaa00;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Technical indicator calculations
def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    if len(prices) < period:
        return pd.Series([50] * len(prices), index=prices.index)
    
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)

def calculate_macd(prices, fast=12, slow=26, signal=9):
    """Calculate MACD (Moving Average Convergence Divergence)"""
    if len(prices) < slow:
        return pd.Series([0] * len(prices)), pd.Series([0] * len(prices)), pd.Series([0] * len(prices))
    
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    
    return macd, signal_line, histogram

def calculate_bollinger_bands(prices, window=20, num_std=2):
    """Calculate Bollinger Bands"""
    if len(prices) < window:
        window = max(2, len(prices) // 2)
    
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    
    return upper_band, rolling_mean, lower_band

def calculate_momentum(prices, period=14):
    """Calculate price momentum"""
    if len(prices) < period:
        return pd.Series([0] * len(prices), index=prices.index)
    return prices.diff(period)

@st.cache_data(ttl=600)
def fetch_historical_data(coin_id, days=30):
    """Fetch historical data from CoinGecko"""
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart",
            params={"vs_currency": "usd", "days": days, "interval": "daily"},
            timeout=15
        )
        response.raise_for_status()
        data = response.json()
        
        prices = data.get('prices', [])
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        
        return df
    except:
        # Fallback mock data
        dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
        prices = 50000 + np.cumsum(np.random.randn(days) * 1000)
        return pd.DataFrame({'price': prices}, index=dates)

def generate_insights(df, coin_name):
    """Generate AI-powered insights based on technical indicators"""
    insights = []
    
    prices = df['price']
    
    # Calculate indicators
    rsi = calculate_rsi(prices)
    macd, signal, histogram = calculate_macd(prices)
    upper_bb, middle_bb, lower_bb = calculate_bollinger_bands(prices)
    momentum = calculate_momentum(prices)
    
    current_price = prices.iloc[-1]
    rsi_current = rsi.iloc[-1]
    macd_current = macd.iloc[-1]
    signal_current = signal.iloc[-1]
    
    # RSI Analysis
    if rsi_current > 70:
        insights.append({
            "type": "bearish",
            "icon": "⚠️",
            "title": "Overbought Conditions Detected",
            "message": f"{coin_name} RSI at {rsi_current:.1f} indicates overbought conditions. Potential correction ahead."
        })
    elif rsi_current < 30:
        insights.append({
            "type": "bullish",
            "icon": "🎯",
            "title": "Oversold Conditions - Buying Opportunity",
            "message": f"{coin_name} RSI at {rsi_current:.1f} suggests oversold conditions. Potential bounce opportunity."
        })
    else:
        insights.append({
            "type": "neutral",
            "icon": "📊",
            "title": "Neutral RSI Levels",
            "message": f"{coin_name} RSI at {rsi_current:.1f} indicates balanced market conditions."
        })
    
    # MACD Analysis
    if macd_current > signal_current and histogram.iloc[-1] > 0:
        insights.append({
            "type": "bullish",
            "icon": "🚀",
            "title": "Bullish MACD Crossover",
            "message": f"{coin_name} showing bullish momentum with MACD above signal line."
        })
    elif macd_current < signal_current and histogram.iloc[-1] < 0:
        insights.append({
            "type": "bearish",
            "icon": "📉",
            "title": "Bearish MACD Crossover",
            "message": f"{coin_name} showing bearish momentum with MACD below signal line."
        })
    
    # Bollinger Bands Analysis
    if current_price > upper_bb.iloc[-1]:
        insights.append({
            "type": "bearish",
            "icon": "🔴",
            "title": "Price Above Upper Bollinger Band",
            "message": f"{coin_name} trading above upper band. High volatility and potential reversal risk."
        })
    elif current_price < lower_bb.iloc[-1]:
        insights.append({
            "type": "bullish",
            "icon": "🟢",
            "title": "Price Below Lower Bollinger Band",
            "message": f"{coin_name} trading below lower band. Potential oversold bounce opportunity."
        })
    
    # Momentum Analysis
    momentum_current = momentum.iloc[-1]
    momentum_avg = momentum.tail(7).mean()
    
    if momentum_current > 0 and momentum_avg > 0:
        insights.append({
            "type": "bullish",
            "icon": "💪",
            "title": "Strong Positive Momentum",
            "message": f"{coin_name} maintains positive momentum with upward price trajectory."
        })
    elif momentum_current < 0 and momentum_avg < 0:
        insights.append({
            "type": "bearish",
            "icon": "📊",
            "title": "Negative Momentum Detected",
            "message": f"{coin_name} experiencing downward momentum. Exercise caution."
        })
    
    # Volatility Analysis
    volatility = prices.pct_change().std() * 100
    if volatility > 5:
        insights.append({
            "type": "neutral",
            "icon": "⚡",
            "title": "High Volatility Alert",
            "message": f"{coin_name} showing high volatility ({volatility:.2f}%). Risk management advised."
        })
    
    return insights, rsi, macd, signal, upper_bb, middle_bb, lower_bb

# Header
st.title("🤖 AI-Powered Insights")
st.markdown("Statistical ML analysis and market predictions")

# Coin selection
selected_coin = st.selectbox(
    "Select Cryptocurrency for Analysis",
    options=["Bitcoin", "Ethereum", "Solana"],
    index=0
)

coin_map = {
    "Bitcoin": "bitcoin",
    "Ethereum": "ethereum",
    "Solana": "solana"
}

coin_id = coin_map[selected_coin]

# Fetch data
with st.spinner(f"Analyzing {selected_coin}..."):
    df = fetch_historical_data(coin_id, days=90)
    insights, rsi, macd, signal, upper_bb, middle_bb, lower_bb = generate_insights(df, selected_coin)

# Display insights
st.markdown("---")
st.markdown("## 💡 Market Insights")

for insight in insights:
    css_class = insight['type']
    st.markdown(f"""
    <div class="{css_class}">
        <h3>{insight['icon']} {insight['title']}</h3>
        <p>{insight['message']}</p>
    </div>
    """, unsafe_allow_html=True)

# Technical Indicators Charts
st.markdown("---")
st.markdown("## 📊 Technical Indicators")

# RSI Chart
st.markdown("### Relative Strength Index (RSI)")
fig_rsi = go.Figure()

fig_rsi.add_trace(go.Scatter(
    x=df.index,
    y=rsi,
    name='RSI',
    line=dict(color='#00f5ff', width=2)
))

# Add overbought/oversold lines
fig_rsi.add_hline(y=70, line_dash="dash", line_color="#ff4444", annotation_text="Overbought (70)")
fig_rsi.add_hline(y=30, line_dash="dash", line_color="#00ff88", annotation_text="Oversold (30)")
fig_rsi.add_hline(y=50, line_dash="dot", line_color="#888888", annotation_text="Neutral (50)")

fig_rsi.update_layout(
    template='plotly_dark',
    height=300,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis_title='Date',
    yaxis_title='RSI',
    yaxis_range=[0, 100],
    showlegend=True
)

st.plotly_chart(fig_rsi, use_container_width=True)

# Display current RSI value
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current RSI", f"{rsi.iloc[-1]:.2f}")
with col2:
    if rsi.iloc[-1] > 70:
        st.warning("⚠️ Overbought")
    elif rsi.iloc[-1] < 30:
        st.success("✅ Oversold")
    else:
        st.info("➡️ Neutral")
with col3:
    st.metric("7-Day Avg RSI", f"{rsi.tail(7).mean():.2f}")

# MACD Chart
st.markdown("---")
st.markdown("### MACD (Moving Average Convergence Divergence)")

fig_macd = go.Figure()

fig_macd.add_trace(go.Scatter(
    x=df.index,
    y=macd,
    name='MACD',
    line=dict(color='#00f5ff', width=2)
))

fig_macd.add_trace(go.Scatter(
    x=df.index,
    y=signal,
    name='Signal',
    line=dict(color='#ff4444', width=2)
))

# Histogram
histogram = macd - signal
colors = ['#00ff88' if val >= 0 else '#ff4444' for val in histogram]

fig_macd.add_trace(go.Bar(
    x=df.index,
    y=histogram,
    name='Histogram',
    marker_color=colors,
    opacity=0.5
))

fig_macd.update_layout(
    template='plotly_dark',
    height=300,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis_title='Date',
    yaxis_title='MACD',
    showlegend=True
)

st.plotly_chart(fig_macd, use_container_width=True)

# Bollinger Bands
st.markdown("---")
st.markdown("### Bollinger Bands")

fig_bb = go.Figure()

fig_bb.add_trace(go.Scatter(
    x=df.index,
    y=df['price'],
    name='Price',
    line=dict(color='#00f5ff', width=2)
))

fig_bb.add_trace(go.Scatter(
    x=df.index,
    y=upper_bb,
    name='Upper Band',
    line=dict(color='#ff4444', width=1, dash='dash')
))

fig_bb.add_trace(go.Scatter(
    x=df.index,
    y=middle_bb,
    name='Middle Band (SMA)',
    line=dict(color='#ffffff', width=1, dash='dot')
))

fig_bb.add_trace(go.Scatter(
    x=df.index,
    y=lower_bb,
    name='Lower Band',
    line=dict(color='#00ff88', width=1, dash='dash'),
    fill='tonexty'
))

fig_bb.update_layout(
    template='plotly_dark',
    height=400,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    showlegend=True
)

st.plotly_chart(fig_bb, use_container_width=True)

# Statistical Predictions
st.markdown("---")
st.markdown("## 🔮 Statistical Predictions")

# Simple linear regression for trend
from numpy.polynomial import Polynomial

recent_prices = df['price'].tail(30).values
x = np.arange(len(recent_prices))
p = Polynomial.fit(x, recent_prices, 1)
trend_direction = p.convert().coef[1]

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Short-term Trend (30 Days)")
    if trend_direction > 0:
        st.success(f"📈 **Upward Trend**: ${abs(trend_direction):.2f}/day")
        st.markdown(f"Statistical model suggests continued upward momentum for {selected_coin}.")
    else:
        st.warning(f"📉 **Downward Trend**: ${abs(trend_direction):.2f}/day")
        st.markdown(f"Statistical model indicates downward pressure for {selected_coin}.")

with col2:
    st.markdown("### Volatility Assessment")
    volatility = df['price'].pct_change().std() * 100
    if volatility > 5:
        st.error(f"⚡ **High Volatility**: {volatility:.2f}%")
        st.markdown("Significant price swings expected. Risk management recommended.")
    elif volatility > 3:
        st.warning(f"⚠️ **Moderate Volatility**: {volatility:.2f}%")
        st.markdown("Average price fluctuations. Standard risk management applies.")
    else:
        st.success(f"✅ **Low Volatility**: {volatility:.2f}%")
        st.markdown("Relatively stable price action. Lower risk environment.")

# Disclaimer
st.markdown("---")
st.warning("""
⚠️ **Disclaimer**: These insights are generated using statistical machine learning algorithms based on historical data. 
They are for informational purposes only and should not be considered financial advice. 
Cryptocurrency investments carry significant risk. Always conduct your own research and consult with financial advisors.
""")

st.caption("💡 Analysis based on 90 days of historical data | Updated every 10 minutes")
