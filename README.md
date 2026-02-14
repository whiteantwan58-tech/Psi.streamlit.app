# 🚀 PSI Sovereign Auto-Updating System
## EVE 1010_WAKE - Quantum Navigation Interface

A comprehensive real-time Solana blockchain monitoring and autonomous system for PSI-Coin built with Streamlit. Features 80% visual design, quantum-themed holographic UI, live data synchronization, and EVE AI integration.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://psi-streamlit-app.streamlit.app/)

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
