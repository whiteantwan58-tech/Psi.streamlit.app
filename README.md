# 🚀 Psi Crypto Dashboard

Professional real-time cryptocurrency analytics dashboard powered by Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

## 🔓 Zero Configuration Required

**Just install and run** - No API keys, no setup, no configuration files needed!

The dashboard uses 100% **FREE public APIs** that require no authentication:
- ✅ CoinGecko API (no key required)
- ✅ CoinCap API (no key required)

## ✨ Features

- 📊 **Real-Time Market Data** - Live BTC, ETH, SOL prices updating every 30 seconds
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

# Run the app - NO CONFIGURATION NEEDED!
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
- **Authentication**: None ✅
- **API Key Required**: ❌ NO

### CoinCap API (Backup)
- **Endpoint**: `https://api.coincap.io/v2/assets`
- **Features**: Real-time prices, historical data
- **Rate Limit**: Unlimited for basic usage
- **Authentication**: None ✅
- **API Key Required**: ❌ NO

### 🔓 API Configuration

**The app requires ZERO configuration!** It works immediately after installation.

- ✅ No API keys needed
- ✅ No signup required
- ✅ No rate limit concerns (smart caching built-in)
- ✅ No authentication tokens
- ✅ 100% free forever

**Want to add more APIs?** See [API_SETUP.md](API_SETUP.md) for instructions on:
- Adding additional free cryptocurrency APIs
- Optional premium API configuration (for future use)
- API troubleshooting and best practices

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
# 🚀 PSI Sovereign Auto-Updating System
## EVE 1010_WAKE - Quantum Navigation Interface

A comprehensive real-time Solana blockchain monitoring and autonomous system for PSI-Coin built with Streamlit. Features 80% visual design, quantum-themed holographic UI, live data synchronization, and EVE AI integration.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://psi-streamlit-app.streamlit.app/)

---

## ⚡ QUICKSTART - One-Tap Deployment

**Ready to deploy? It's this easy:**

1. Go to **https://share.streamlit.io**
2. Sign in with Google
3. Click **"New app"**
4. Select: Repository `whiteantwan58-tech/Psi.streamlit.app`, Branch `main`, File `streamlit_app.py`
5. Click **"Deploy!"**

**That's it!** Your app auto-runs with:
- ✅ Real-time PSI token monitoring
- ✅ Auto-refresh every 30 seconds
- ✅ EVE AI chat (API key pre-configured)
- ✅ 6 interactive tabs with quantum theme
- ✅ Self-healing error recovery
- ✅ Mobile-optimized design

**📖 Full Instructions**: See [QUICKSTART.md](QUICKSTART.md) for detailed step-by-step guide.

---

## ✨ Features

### 🎨 Visual Design (80% Visual / 20% Text)
- 🌌 **Holographic Quantum Theme** - Animated gradients, neon effects, and glowing elements
- 💫 **6 Interactive Tabs** - Seamless navigation with visual indicators
- 📊 **HD Charts & Visualizations** - Plotly-powered interactive graphs
- 🎯 **Progress Bars with Emoji** - Visual status tracking
- ⚡ **Auto-Refresh UI** - Live updates every 30 seconds
- 📱 **Mobile-Optimized** - Responsive design for all devices

### 🪙 PSI Coin Monitoring
- 💰 **Real-time Token Price** - Live tracking from Solana blockchain
  - Token Address: `7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump`
- 👛 **Wallet Balance Tracking** - Monitor SOL balance in real-time
  - Wallet Address: `b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH`
- 🌐 **CEC/WAM Live Data System** - Wide Area Monitoring with Google Sheets integration
  - Real-time data synchronization from Google Sheets
  - Color-coded status system (PERFECT 🟢, TODO 🟡, ACTIVE 🔵, STABLE ⚪)
  - Status distribution analytics
  - Auto-refresh every 5 minutes
  - Data export capabilities
- 📊 **Automatic Activity Logging** - Track all system activities automatically
  - Real-time logging of all operations to CSV
  - Filter and search log entries
  - Export logs for analysis
  - Statistics dashboard (success, warnings, errors)
  - Performance monitoring
- 📁 **CSV Data Management** - Load and manage pump.fun.csv data
- 💾 **Data Export** - Export holdings and metrics to CSV
- 🔄 **Auto-Refresh** - Automatic updates every 30 seconds
- 📈 **System Health Metrics** - Monitor connection status and data freshness
- 🎨 **Responsive Layout** - Clean, modern interface with enhanced visuals
- 📈 **Bonding Curve Visualization** - Color-coded progress to 100%
- 💎 **Internal Value Tracking** - $155.50 → $34.1M progression
- 👛 **Wallet Balance Monitoring** - SOL balance tracking
  - Wallet: `b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH`
- 📊 **Price History Charts** - 30-day trajectory visualization

### 📊 CEC/WAM Master Ledger
- 📋 **Auto-Import CSV Data** - Supports multiple data sources
- 🎨 **Color-Coded Status System**:
  - 🟢 **PERFECT** - System operating optimally
  - 🟡 **TODO** - Items requiring attention
  - 🔵 **ACTIVE** - Currently processing
  - ⚪ **STABLE** - System in stable state
- 🔬 **Quantum Calculations**:
  - Golden Ratio (Φ = 1.618)
  - Quantum Constant (3.32E-36)
  - Black Hole Metric (1.75E+21)
- 📅 **Time-Series Tracking** - Days since Nov 6, 2024
- 💾 **Export Capabilities** - CSV download, Google Sheets (planned)

### 🌌 EVE AI System
- 💬 **Live Chat Interface** - Context-aware conversational AI
- 🤖 **GROQ API Integration** - Free-tier unlimited access
- 📊 **System Status Reporting** - Real-time health metrics
- ⚡ **Quick Action Buttons** - One-click common queries
- 🗨️ **Chat History** - Persistent conversation tracking
- 🎯 **Quantum-Themed Responses** - EVE 1010_WAKE personality

### 🔐 Security & Authentication (Placeholder)
- 🔒 **Biometric Lock Screen** - Visual authentication interface
- 📸 **Camera Integration Prep** - MediaDevices API ready
- 👤 **User Access Control** - whiteantwan58-tech & eve authorized
- 🛡️ **Activity Logging** - All operations tracked to CSV

### 🎥 Live Feeds (Placeholders)
- 📹 **Camera Feed Interface** - Browser-based access prep
- 🔭 **Space Telescope Integration** - NASA API placeholder
- 🌍 **Additional Feeds** - Crime maps, radio waves, navigation

### 🗺️ Navigation & Visualization
- ✨ **Star Navigation Maps** - Quantum navigation interface
- 🕳️ **Black Hole Simulation** - Entry/exit calculations
- 📡 **Quantum Communications** - EVE chat interface
- 🎨 **3D Holographic Placeholders** - Future enhancements

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) GROQ API key for future AI features

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/whiteantwan58-tech/Psi.streamlit.app.git
   cd Psi.streamlit.app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables (Optional)**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your configuration:
   ```
   # Optional: GROQ API key for future AI features
   GROQ_API_KEY=your_actual_groq_api_key_here
   
   # Optional: CEC/WAM System - Google Sheets URL for live data
   CEC_WAM_SHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
   ```
   
   > **Note**: 
   > - The GROQ_API_KEY is optional and reserved for future AI features.
   > - The CEC_WAM_SHEET_URL enables the live data monitoring system.

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Access the app**
   
   Open your browser and navigate to: `http://localhost:8501`

## 🌐 Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Ensure all changes are committed and pushed to GitHub
2. Verify `.gitignore` is preventing `.env` and `.csv` files from being committed

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `whiteantwan58-tech/Psi.streamlit.app`
5. Branch: `main` (or your preferred branch)
6. Main file path: `streamlit_app.py`
7. Click "Deploy"

### Step 3: Configure Secrets (Optional)

If you want to use GROQ features or enable CEC/WAM live data:

1. In Streamlit Cloud dashboard, click on your app
2. Go to "Settings" → "Secrets"
3. Add your secrets in TOML format:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   CEC_WAM_SHEET_URL = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
   ```
4. Save and restart the app

> **Note**: For CEC/WAM to work, your Google Sheet must be publicly accessible (Share → Anyone with link can view)

## 🔒 Security Notes

### Environment Variables

- **Never commit `.env` files** to version control
- Use `.env.example` as a template only (contains no real secrets)
- In production (Streamlit Cloud), use the Secrets management feature
- The `.gitignore` is configured to exclude `.env` files automatically

### API Keys

- GROQ_API_KEY is optional and loaded from environment variables only
- No API keys are hardcoded in the source code
- The app displays a "🔑 API Key Loaded" indicator when a valid key is present

### Data Files

- CSV files are excluded from Git to prevent accidental exposure of sensitive data
- Only `example.csv` would be tracked if present
- Ensure CSV files don't contain sensitive personal information before loading

## 🌐 CEC/WAM Live Data System

### What is CEC/WAM?

**CEC/WAM (Wide Area Monitoring)** is a real-time data monitoring and aggregation system that enables:

- **Live Data Synchronization**: Automatically fetches data from Google Sheets every 5 minutes
- **Color-Coded Status System**: Visual indicators for quick status assessment
  - 🟢 **PERFECT**: System operating optimally
  - 🟡 **TODO**: Items requiring attention
  - 🔵 **ACTIVE**: Currently processing or in progress
  - ⚪ **STABLE**: System in stable state
- **Real-time Analytics**: Status distribution metrics and trends
- **Data Export**: Download live data for offline analysis
- **Auto-Refresh**: Keeps data fresh with automatic periodic updates

### Setting Up CEC/WAM

1. **Create a Google Sheet** with your monitoring data
   - Include a "Status" column with values: PERFECT, TODO, ACTIVE, or STABLE
   - Add any additional columns for your data

2. **Make the sheet publicly accessible**
   - Click "Share" in your Google Sheet
   - Set to "Anyone with the link can view"

3. **Get the sheet URL**
   - Copy the full Google Sheets URL
   - Example: `https://docs.google.com/spreadsheets/d/1ABC123xyz/edit`

4. **Configure the application**
   - Local: Add `CEC_WAM_SHEET_URL` to your `.env` file
   - Streamlit Cloud: Add to Secrets in TOML format

5. **Restart and access**
   - Restart the application
   - Navigate to the "🌐 CEC/WAM Live" tab

### CEC/WAM Data Format

Your Google Sheet should include these columns:

```csv
Status,Component,Description,Value,Timestamp
PERFECT,System A,Operating normally,100,2026-02-14 10:00:00
TODO,System B,Requires update,85,2026-02-14 10:00:00
ACTIVE,System C,Processing data,92,2026-02-14 10:00:00
STABLE,System D,Idle state,78,2026-02-14 10:00:00
```

The "Status" column is required for color-coding. All other columns are flexible based on your needs.

## 📊 Activity Logging System

### What is Activity Logging?

The application includes an **Automatic Activity Logging System** that tracks all operations and saves them to CSV files for analysis and monitoring.

### Features

- **Automatic Logging**: All system activities are automatically logged
- **CSV Storage**: Logs saved to `activity_log.csv` (excluded from git)
- **Real-time Tracking**: Monitor data fetches, API calls, and operations
- **Filter & Search**: Filter logs by status and action type
- **Statistics Dashboard**: View success rates, warnings, and errors
- **Export Capabilities**: Download filtered or complete logs
- **Performance Monitoring**: Track system health and response times

### Logged Activities

The system automatically logs:
- Wallet balance queries
- Token metadata requests
- Price updates
- CEC/WAM data synchronization
- CSV file operations
- All API interactions

### Log File Structure

```csv
timestamp,action,details,status
2026-02-14 10:00:00,WALLET_BALANCE,Balance: 1.2345 SOL,SUCCESS
2026-02-14 10:00:05,TOKEN_METADATA,Symbol: PSI Name: PSI-Coin,SUCCESS
2026-02-14 10:00:10,TOKEN_PRICE,Price: $0.001234,SUCCESS
2026-02-14 10:00:15,CEC_WAM_SYNC,Loaded 25 records,SUCCESS
```

### Using the Activity Log Tab

1. Navigate to the "📊 Activity Log" tab
2. View statistics: total entries, successes, warnings, errors
3. Use filters to find specific activities
4. Export logs for offline analysis
5. Clear logs when needed (careful - this is permanent!)

### Privacy Note

Activity logs are stored locally and excluded from version control. They contain only system operation data, not sensitive personal information.

## 📁 CSV File Requirements

The app can load CSV files from the repository root directory. Expected format for `pump.fun.csv`:

```csv
token_address,symbol,name,price,market_cap,volume_24h
7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump,PSI,PSI-Coin,0.00123,500000,125000
```

Place your CSV files in the root directory. The app will automatically detect and load them.

## 🔧 Technical Details

### APIs Used

- **Solana RPC**: `https://api.mainnet-beta.solana.com` - For blockchain queries
- **Solscan API**: Public endpoints for token metadata and pricing
- Rate limiting and caching (30-60 second TTL) are implemented

### Dependencies

- `streamlit>=1.32.0` - Web application framework
- `pandas>=2.0.0` - Data manipulation and analysis
- `requests>=2.31.0` - HTTP requests for API calls
- `solana>=0.30.0` - Solana blockchain client library
- `numpy>=1.24.0` - Numerical computing for calculations
- `plotly>=5.18.0` - Interactive HD visualizations
- `python-dotenv>=1.0.0` - Environment variable management

### Caching Strategy

- Token metadata: 60-second cache
- Wallet balance: 30-second cache
- Auto-refresh: 30-second interval
- Graceful error handling with fallback values

## 🎯 Monitored Addresses

### PSI-Coin Token
- **Address**: `7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump`
- **Network**: Solana Mainnet
- **Type**: SPL Token

### Wallet
- **Address**: `b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH`
- **Network**: Solana Mainnet
- **Purpose**: Balance monitoring

> These are public blockchain addresses and safe to include in documentation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub](https://github.com/whiteantwan58-tech/Psi.streamlit.app/issues)
- Check existing issues for solutions

## 🔄 Version History

### v2.1.0 (Current - Enhanced with Auto-Logging)
- ✅ Added automatic activity logging system
- ✅ Real-time activity tracking to CSV
- ✅ Activity log dashboard with statistics
- ✅ Filter and export log capabilities
- ✅ Enhanced visual feedback and UI improvements
- ✅ Success indicators with timestamps
- ✅ Comprehensive error handling
- ✅ Performance monitoring features

### v2.0.0 (CEC/WAM Enabled)
### v3.0.0 (Current - Sovereign System) ✨
- ✅ **Complete Rewrite**: 1,000+ lines of production code
- ✅ **Fixed Critical Error**: Removed `VIDEO source` syntax error
- ✅ **80% Visual Design**: Holographic quantum-themed UI with animations
- ✅ **6 Functional Tabs**: PSI Monitor, EVE System, Master Ledger, Live Feeds, Nav Maps, Quantum Comm
- ✅ **Real Solana Integration**: Live blockchain queries with graceful fallbacks
- ✅ **Bonding Curve**: Dynamic progress tracking to 100%
- ✅ **EVE AI Chat**: Context-aware responses with GROQ API
- ✅ **Activity Logging**: All operations logged to CSV
- ✅ **CEC/WAM Framework**: Auto-import with quantum calculations
- ✅ **Auto-Refresh**: 30-second blockchain updates
- ✅ **Mobile-Optimized**: Responsive design for all devices
- ✅ **Error Handling**: Graceful fallbacks for all API calls
- ✅ **Documentation**: Complete deployment guide and examples

### v2.0.0 (Previous - CEC/WAM Enabled)
- ✅ Added CEC/WAM (Wide Area Monitoring) live data system
- ✅ Google Sheets integration for real-time data synchronization
- ✅ Color-coded status indicators (PERFECT, TODO, ACTIVE, STABLE)
- ✅ Status distribution analytics and metrics
- ✅ Auto-refresh every 5 minutes for live data
- ✅ Data export functionality for CEC/WAM data
- ✅ Enhanced documentation and configuration options
- ✅ Fixed all existing code errors

### v1.0.0
- Initial release with full Solana blockchain monitoring
- PSI-Coin token tracking
- Real-time wallet balance monitoring
- CSV data integration
- Auto-refresh functionality
- Security best practices implementation
