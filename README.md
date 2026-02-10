# 🚀 Psi Crypto Dashboard

Professional real-time cryptocurrency analytics dashboard powered by Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

## ✨ Features

- 📊 **Real-Time Market Data** - Live BTC, SOL, ETH prices updating every 30 seconds
- 📈 **Advanced Charts** - Interactive Plotly visualizations with zoom and pan
- 🤖 **AI-Powered Insights** - Statistical ML analysis with RSI, MACD, and Bollinger Bands
- 💼 **Portfolio Tracking** - Monitor your crypto holdings and performance
- 🌙 **Beautiful Dark Theme** - Eye-friendly design with glassmorphism effects
- ⚡ **Auto-Refresh** - Seamless data updates every 30 seconds
- 🔓 **No API Keys Required** - 100% free forever, no subscriptions needed
- 💾 **Smart Caching** - Optimized performance with automatic fallback to cached data

## 🚀 Quick Start

### Run Locally

```bash
# Clone the repository
git clone https://github.com/whiteantwan58-tech/Psi.streamlit.app.git
cd Psi.streamlit.app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Deploy to Streamlit Cloud (Recommended)

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app" and select your forked repository
5. Set the main file path to `streamlit_app.py`
6. Click "Deploy"
7. Your app will be live in ~2 minutes! 🎉

The app runs 24/7 on Streamlit Cloud with automatic updates when you push to GitHub.

## 📊 Dashboard Pages

### 1. 🏠 Home
Welcome page with feature overview and navigation guide.

### 2. 📊 Market Overview
- Real-time prices for Bitcoin, Ethereum, and Solana
- 24-hour price changes with color indicators
- Market cap and volume data
- Large metric cards with trend arrows
- Auto-refreshing every 30 seconds

### 3. 📈 Advanced Analytics
- Interactive price charts with Plotly
- Historical data visualization (7d, 30d, 90d)
- Candlestick charts for technical analysis
- Volume analysis
- Price correlation heatmaps
- Moving averages (7-day and 30-day)
- Statistical summaries

### 4. 🤖 AI Insights
- **RSI (Relative Strength Index)** - Identifies overbought/oversold conditions
- **MACD (Moving Average Convergence Divergence)** - Momentum and trend analysis
- **Bollinger Bands** - Volatility and price range analysis
- Auto-generated market insights:
  - "Bitcoin momentum strengthening - 14-day RSI at 62"
  - "Solana shows bullish divergence"
  - "High volatility detected - risk management advised"
- Statistical trend predictions
- Volatility assessments

### 5. 💼 Portfolio Tracker
- Add cryptocurrency holdings (BTC, ETH, SOL)
- Calculate total portfolio value in real-time
- Profit/loss tracking with percentage changes
- Performance metrics by asset
- Portfolio allocation pie charts
- Best/worst performer identification
- Individual holding management

## 🔗 APIs Used (All FREE)

### CoinGecko API (Primary)
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **Features**: Real-time prices, market caps, 24h volumes, price changes
- **Rate Limit**: 50 calls/minute (sufficient for this app)
- **No API Key Required**: ✅

### CoinCap API (Backup)
- **Endpoint**: `https://api.coincap.io/v2/assets`
- **Features**: Real-time prices, historical data
- **Rate Limit**: Unlimited for basic usage
- **No API Key Required**: ✅

## 🛠️ Technical Stack

- **Framework**: Streamlit 1.31+
- **Visualization**: Plotly 5.18+
- **Data Processing**: Pandas 2.1+, NumPy 1.26+
- **API Requests**: Requests 2.31+
- **Additional**: Altair 5.2+

## ⚙️ Key Features Explained

### Auto-Refresh System
The dashboard automatically refreshes data every 30 seconds using a combination of:
- JavaScript-based client-side refresh
- Streamlit's `st.rerun()` mechanism
- Smart caching with TTL (Time To Live)

### Error Handling
- Automatic fallback to cached data if APIs are unavailable
- Graceful degradation with mock data
- User-friendly error messages
- Timeout protection (10-15 seconds)

### Performance Optimization
- Data caching with 5-10 minute TTL
- Efficient API calls
- Lazy loading of heavy computations
- Optimized chart rendering

### Statistical ML (No Cloud AI)
All machine learning insights are computed locally using:
- NumPy for statistical calculations
- Pandas for data manipulation
- Custom algorithms for RSI, MACD, Bollinger Bands
- Linear regression for trend analysis
- No external AI APIs or services required

## 📱 Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS/Android)

## 🎨 Customization

### Change Color Scheme
Edit the CSS in `streamlit_app.py`:
```python
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #YOUR_COLOR_1, #YOUR_COLOR_2);
        }
    </style>
""", unsafe_allow_html=True)
```

### Add More Cryptocurrencies
Update the API calls in page files:
```python
"ids": "bitcoin,ethereum,solana,cardano,polygon"
```

### Adjust Refresh Rate
Modify the JavaScript timeout in Market Overview page:
```javascript
setTimeout(function(){ window.location.reload(); }, 30000); // 30 seconds
```

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt --upgrade
```

### API rate limiting
The app uses caching to minimize API calls. If you hit rate limits:
- Increase cache TTL in `@st.cache_data(ttl=600)`
- Use backup CoinCap API

### Slow loading
- Check your internet connection
- Clear Streamlit cache: Settings → Clear Cache
- Reduce historical data period (7d instead of 90d)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

MIT License - Use freely for personal or commercial projects!

## ⚠️ Disclaimer

This dashboard is for informational purposes only. The data and insights provided should not be considered financial advice. Cryptocurrency investments carry significant risk. Always conduct your own research and consult with qualified financial advisors before making investment decisions.

## 🙏 Credits

- Data provided by [CoinGecko](https://www.coingecko.com/) and [CoinCap](https://coincap.io/)
- Built with [Streamlit](https://streamlit.io/)
- Charts powered by [Plotly](https://plotly.com/)

## 📞 Support

- 🐛 Issues: [GitHub Issues](https://github.com/whiteantwan58-tech/Psi.streamlit.app/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/whiteantwan58-tech/Psi.streamlit.app/discussions)

---

Made with ❤️ using Streamlit | Star ⭐ this repo if you find it useful!
