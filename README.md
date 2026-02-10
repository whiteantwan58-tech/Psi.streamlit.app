# 🚀 PSI-Coin Solana Blockchain Monitor

A real-time Solana blockchain monitoring application for PSI-Coin (EVE 1010_WAKE) built with Streamlit. This app provides live tracking of token prices, wallet balances, and blockchain data integration.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://psi-streamlit-app.streamlit.app/)

## ✨ Features

- 🔗 **Real-time Solana Blockchain Integration** - Connect to Solana mainnet-beta
- 💰 **PSI-Coin Token Monitoring** - Track token metadata and pricing
  - Token Address: `7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump`
- 👛 **Wallet Balance Tracking** - Monitor SOL balance in real-time
  - Wallet Address: `b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH`
- 📊 **Live Data Fetching** - Integration with Solscan API
- 📁 **CSV Data Management** - Load and manage pump.fun.csv data
- 💾 **Data Export** - Export holdings and metrics to CSV
- 🔄 **Auto-Refresh** - Automatic updates every 30 seconds
- 📈 **System Health Metrics** - Monitor connection status and data freshness
- 🎨 **Responsive Layout** - Clean, modern interface with metrics display

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
   
   Edit `.env` and add your GROQ API key (if needed):
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
   
   > **Note**: The GROQ_API_KEY is optional. The app will work without it as it's reserved for future AI features.

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

If you want to use GROQ features:

1. In Streamlit Cloud dashboard, click on your app
2. Go to "Settings" → "Secrets"
3. Add your secrets in TOML format:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
4. Save and restart the app

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

### v1.0.0 (Current)
- Initial release with full Solana blockchain monitoring
- PSI-Coin token tracking
- Real-time wallet balance monitoring
- CSV data integration
- Auto-refresh functionality
- Security best practices implementation
