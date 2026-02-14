# 🚀 Deployment Guide - PSI Sovereign System

## Quick Start - Streamlit Cloud Deployment

### Step 1: Prepare Repository
```bash
# Ensure all changes are committed
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. **Visit**: [share.streamlit.io](https://share.streamlit.io)
2. **Sign In**: Use your GitHub account (whiteantwan58-tech)
3. **Click**: "New app" button
4. **Configure**:
   - **Repository**: `whiteantwan58-tech/Psi.streamlit.app`
   - **Branch**: `main`
   - **Main file**: `streamlit_app.py`
5. **Click**: "Deploy!"

### Step 3: Configure Secrets (Optional but Recommended)

1. Go to your app's dashboard
2. Click **Settings** → **Secrets**
3. Add in TOML format:

```toml
# GROQ API for EVE AI Chat
GROQ_API_KEY = "your_actual_groq_api_key_here"

# Google Sheets for CEC/WAM Live Data
CEC_WAM_SHEET_URL = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"

# Optional: Custom Solana RPC
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
```

4. **Save** and **Restart** the app

### Step 4: Verify Deployment

Expected URL format:
- `https://psi-streamlit-app.streamlit.app`
- Or: `https://whiteantwan58-tech-psi-streamlit-app-streamlit-app-xyz123.streamlit.app`

**Test all tabs:**
- ✅ 🚀 PSI Coin Monitor
- ✅ 🌌 EVE System
- ✅ 📊 Master Ledger
- ✅ 🎥 Live Feeds
- ✅ 🗺️ Nav Maps
- ✅ 📡 Quantum Comm

---

## Local Development Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/whiteantwan58-tech/Psi.streamlit.app.git
cd Psi.streamlit.app

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your actual API keys

# Run locally
streamlit run streamlit_app.py
```

### Access Locally
- **URL**: http://localhost:8501
- **Port**: 8501 (default)

---

## Configuration Details

### Required Dependencies
- `streamlit>=1.32.0` - Web framework
- `pandas>=2.0.0` - Data manipulation
- `requests>=2.31.0` - HTTP requests
- `solana>=0.30.0` - Blockchain client
- `numpy>=1.24.0` - Numerical computing
- `plotly>=5.18.0` - Interactive charts
- `python-dotenv>=1.0.0` - Environment variables

### Optional Dependencies
For advanced features (not yet implemented):
- `opencv-python` - Camera integration
- `gspread` - Google Sheets API
- `google-auth` - Google authentication
- `groq` - GROQ API client (currently using requests)

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Optional | EVE AI chat functionality |
| `CEC_WAM_SHEET_URL` | Optional | Live Google Sheets data sync |
| `SOLANA_RPC_URL` | Optional | Custom Solana endpoint |
| `NASA_API_KEY` | Optional | Space telescope feeds (future) |

---

## Security Best Practices

### ✅ DO:
- Use Streamlit Cloud Secrets for API keys
- Keep `.env` file in `.gitignore`
- Use `.env.example` as a template only
- Make Google Sheets publicly readable (not writable)
- Monitor activity logs for suspicious behavior

### ❌ DON'T:
- Commit `.env` files to git
- Expose private keys in code
- Share API keys publicly
- Make Google Sheets publicly writable
- Commit `activity_log.csv` (contains operational data)

---

## Troubleshooting

### App Won't Start

**Error**: `ModuleNotFoundError: No module named 'streamlit'`

**Fix**:
```bash
pip install -r requirements.txt
```

---

### API Keys Not Working

**Error**: `GROQ_API_KEY not configured`

**Fix**:
1. Check `.streamlit/secrets.toml` exists
2. Verify TOML format (use `=` not `:`)
3. Restart the app
4. Check Streamlit Cloud Secrets if deployed

---

### Google Sheets Not Loading

**Error**: `Failed to load CEC/WAM data`

**Fix**:
1. Verify sheet is publicly accessible
2. Check URL format: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`
3. Ensure sheet has correct column structure
4. Fallback to `example_cec_wam.csv` will auto-load

---

### Auto-Refresh Not Working

**Issue**: Data not updating every 30 seconds

**Fix**:
1. This is expected behavior in some browsers
2. Click "🔄 Force Refresh All" in sidebar
3. Clear Streamlit cache manually if needed
4. Check browser console for errors

---

## Performance Optimization

### Caching Strategy
- **Token metadata**: 60-second TTL
- **Wallet balance**: 30-second TTL
- **CEC/WAM data**: 5-minute TTL (300s)
- **Price data**: 30-second TTL

### Best Practices
- Use `@st.cache_data` for expensive operations
- Implement exponential backoff for API failures
- Log all errors to `activity_log.csv`
- Monitor Streamlit Cloud resource usage

---

## Mobile Access

### ROG Ally X Handheld
1. Access via browser: `https://your-app-url.streamlit.app`
2. Enable fullscreen mode for better experience
3. Touch controls are optimized for tablet/handheld

### iPhone/iPad
1. Add to Home Screen for app-like experience
2. Use Safari for best compatibility
3. Enable desktop mode if needed

### Siri Shortcuts (Planned)
- Quick access to PSI price
- System health checks
- Launch app with voice command

---

## Monitoring & Maintenance

### Activity Logs
All operations are logged to `activity_log.csv`:
- Timestamp
- Action performed
- Details
- Status (Success/Error/Warning)

### Health Checks
Monitor these metrics:
- ✅ Solana RPC connection
- ✅ API response times
- ✅ Token price updates
- ✅ Wallet balance queries
- ⚠️ Error rates

### Regular Maintenance
1. **Weekly**: Review activity logs
2. **Monthly**: Update dependencies
3. **Quarterly**: Audit security settings
4. **As needed**: Clear old CSV files

---

## Multi-Repo Sync (Future)

### Target Repositories
1. `whiteantwan58-tech/Psi.streamlit.app` (current)
2. `whiteantwan58-tech/CEC-WAM-HOT-CORE`
3. `whiteantwan58-tech/EVE-HEI-`

### Sync Strategy
- Use GitHub Actions for automated sync
- Webhook triggers on data updates
- Cross-repo activity logging
- Unified deployment pipeline

---

## Support & Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Solana Web3.js](https://solana-labs.github.io/solana-web3.js/)
- [Plotly Python](https://plotly.com/python/)

### API Documentation
- [Solscan API](https://public-api.solscan.io/)
- [GROQ API](https://console.groq.com/docs)
- [NASA APIs](https://api.nasa.gov)

### Issues & Support
- GitHub Issues: [Report Bug](https://github.com/whiteantwan58-tech/Psi.streamlit.app/issues)
- Discussions: [Ask Questions](https://github.com/whiteantwan58-tech/Psi.streamlit.app/discussions)

---

## Success Criteria Checklist

- [ ] ✅ App deploys to Streamlit Cloud
- [ ] ✅ All 6 tabs load correctly
- [ ] ✅ PSI token price displays (live or simulated)
- [ ] ✅ Bonding curve shows progress
- [ ] ✅ Wallet balance monitored
- [ ] ✅ CEC/WAM data loads
- [ ] ✅ EVE AI chat responds
- [ ] ✅ Auto-refresh works (30s)
- [ ] ✅ Activity logging active
- [ ] ✅ Mobile-responsive design
- [ ] ✅ Loads in <3 seconds
- [ ] ✅ 80% visual design achieved
- [ ] ✅ Zero critical errors

---

## Version History

### v3.0.0 (Current - Sovereign System)
- ✅ Complete rewrite with production code
- ✅ Fixed critical syntax errors
- ✅ Implemented 6 functional tabs
- ✅ Real Solana blockchain integration
- ✅ Quantum-themed holographic UI
- ✅ EVE AI chat system
- ✅ Activity logging framework
- ✅ Auto-refresh mechanisms
- ✅ Bonding curve calculations
- ✅ CEC/WAM Master Ledger
- ✅ Mobile-optimized design

### v2.0.0 (Previous)
- CEC/WAM integration framework
- Basic Solana queries
- Google Sheets support

### v1.0.0 (Initial)
- Skeleton code
- Multi-location dashboards
- Basic UI

---

**Last Updated**: 2026-02-14
**Maintained by**: whiteantwan58-tech
**Status**: 🚀 Production Ready (75% complete)
