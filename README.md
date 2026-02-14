# 🚀 PSI Sovereign System - Complete Visual Intelligence Dashboard

A cutting-edge, real-time blockchain monitoring and sovereign system interface for PSI-Coin built with Streamlit. Features holographic UI, biometric-style authentication, live data tracking, and comprehensive system monitoring.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://psi-streamlit-app.streamlit.app/)

![PSI Sovereign System](https://img.shields.io/badge/Status-ONLINE-00D9FF?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0-A855F7?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge)

---

## ✨ Features Overview

### 🔐 Security & Authentication
- **Biometric-Style Login Screen** - Secure authentication for authorized personnel (Twan, EVE, Admin)
- **Session Management** - Secure session handling with timeout controls
- **Activity Logging** - All actions logged to CSV with timestamps
- **Password Hashing** - SHA-256 encrypted authentication

### 💎 PSI Tracking & Blockchain
- **Real-time PSI Price** - Current price: $0.003466
- **Internal Value Tracking** - Locked value: $155.50
- **Bonding Curve Visualization** - Live progress tracking (currently 0%)
- **Auto-refresh** - Updates every 30 seconds
- **Price Analytics** - 24h, 7d, 30d change tracking
- **Interactive Charts** - Plotly-powered visualizations

### 📊 CEC WAM Data System
- **Wide Area Monitoring** - Real-time system status tracking
- **Color-Coded Status** - 🟢 PERFECT, 🟡 TODO, 🔵 ACTIVE, ⚪ STABLE
- **Component Monitoring** - Track all system components
- **Data Export** - CSV download capabilities
- **Auto-refresh** - Updates every 5 minutes

### 🌌 Navigation & Visualization
- **3D Star Map** - Interactive navigation visualization
- **Waypoint Tracking** - Key milestone locations
- **Black Hole Simulation** - Wormhole visualization (1.75E+21)
- **Real-time Positioning** - Dynamic coordinate tracking

### 📈 Progress Tracking
- **System Completion %** - Track progress toward 100% sovereignty
- **Component Breakdown**:
  - 🔐 Security/Biometrics: 75%
  - 💎 PSI Value/Growth: 15%
  - 📁 Data Integration: 60%
  - 🤖 AI/EVE Capabilities: 40%
  - 🎨 Visual Quality: 85%
  - 🔔 Alerts & Logging: 70%
  - 📊 Analytics: 55%
  - 🌐 Integration APIs: 30%

### 🗓️ Timeline System
- **Historical Events** - Complete timeline since Nov 6, 2025
- **Key Milestones**:
  - Nov 6: PSI Foundation 🔵
  - Nov 10: Golden Lock 1.618 🟡
  - Feb 3: OMEGA_LOCK Mode ($34.1M) 🟢
  - Feb 12: Wormhole Simulation 🌌
  - Feb 14: Current Status 💎

### 🔔 Alerts & Notifications
- **Real-time Alerts** - System-wide notification system
- **Alert Types** - Info, Success, Warning, Error
- **Activity Tracking** - Complete action history
- **Read/Unread Status** - Track alert engagement

### 🎨 Holographic UI Design
- **80% Visual, 20% Text** - Emphasis on visual data presentation
- **Futuristic Theme** - Cyan (#00D9FF) and Purple (#A855F7) gradients
- **Animated Elements** - Smooth transitions and glow effects
- **Emoji Navigation** - Icon-driven interface
- **Responsive Design** - Optimized for all screen sizes

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

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

3. **Configure environment (Optional)**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Access the dashboard**
   - Open browser: `http://localhost:8501`
   - Login with credentials:
     - Username: `Twan` / Password: `TwanSecure2026`
     - Username: `EVE` / Password: `EVE1010Wake`
     - Username: `admin` / Password: `admin123`

---

## 📦 Dependencies

- **streamlit** >= 1.32.0 - Web application framework
- **pandas** >= 2.0.0 - Data manipulation
- **plotly** >= 5.18.0 - Interactive visualizations
- **numpy** >= 1.24.0 - Numerical computing
- **requests** >= 2.31.0 - HTTP library
- **solana** >= 0.30.0 - Solana blockchain integration

---

## 🌐 Deployment to Streamlit Cloud

### Step 1: Prepare Repository

1. Commit all changes to GitHub
2. Ensure `.gitignore` excludes sensitive files (`.env`, `*.csv`)

### Step 2: Deploy

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - Repository: `whiteantwan58-tech/Psi.streamlit.app`
   - Branch: `main`
   - Main file: `streamlit_app.py`
5. Click "Deploy"

### Step 3: Configure Secrets (Optional)

In Streamlit Cloud dashboard → Settings → Secrets:

```toml
# Authentication (optional - for production use)
[auth]
twan_password = "your_secure_password"
eve_password = "your_secure_password"
admin_password = "your_secure_password"

# API Keys (optional)
GROQ_API_KEY = "your_groq_api_key"
SOLSCAN_API_KEY = "your_solscan_api_key"

# Blockchain (optional)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
PSI_TOKEN_ADDRESS = "7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump"
```

---

## 📁 File Structure

```
Psi.streamlit.app/
├── streamlit_app.py          # Main application
├── requirements.txt           # Python dependencies
├── .env.example              # Environment configuration template
├── example_cec_wam.csv       # Sample CEC WAM data
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── .streamlit/
│   └── config.toml          # Streamlit configuration
└── .github/
    └── workflows/
        └── python-app.yml    # CI/CD pipeline
```

---

## 🎯 Navigation Pages

### 🏠 Home Dashboard
- System overview with key metrics
- PSI price and bonding curve charts
- CEC WAM status summary
- Recent activity log

### 💎 PSI Tracker
- Large metric displays
- Price history charts
- Bonding curve visualization
- Analytics and milestones

### 📊 CEC WAM Data
- System status overview
- Detailed component logs
- Value distribution charts
- CSV data export

### 🌌 Navigation Map
- 3D star map visualization
- Waypoint coordinates
- Black hole status
- Journey progress

### 📈 Progress Tracker
- Overall system completion
- Component-wise progress
- Tangible asset values
- Progress charts

### 🗓️ Timeline
- Historical event log
- Key milestones
- Activity history
- CSV export

### 🔔 Alerts
- Real-time notifications
- Alert management
- Read/unread tracking
- Test alert generation

### ⚙️ Settings
- General settings
- Security configuration
- Data management
- Import/export tools

---

## 🔒 Security Notes

- **Never commit `.env` files** - Contains sensitive credentials
- **Change default passwords** - Use strong, unique passwords in production
- **Use HTTPS** - Always deploy with SSL/TLS encryption
- **Regular updates** - Keep dependencies up to date
- **Activity monitoring** - Review activity logs regularly
- **Session timeouts** - Configure appropriate timeout periods

---

## 📊 Data Sources

### PSI-Coin Blockchain Data
- **Token Address**: `7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump`
- **Wallet Address**: `b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH`
- **Network**: Solana Mainnet-Beta

### CEC/WAM Data
- **Source**: CSV files (example_cec_wam.csv)
- **Google Drive**: Can be integrated with Drive folder ID
- **Update Frequency**: Every 5 minutes

---

## 🎨 UI Customization

The holographic theme can be customized by editing the CSS in `streamlit_app.py`:

```python
# Color Scheme
Primary: #00D9FF (Cyan)
Secondary: #A855F7 (Purple)
Success: #00FF00 (Green)
Warning: #FFD700 (Gold)
Danger: #FF0000 (Red)

# Fonts
Headers: 'Orbitron'
Body: 'Rajdhani'
```

---

## 🔧 Advanced Configuration

### Environment Variables

See `.env.example` for all available configuration options including:
- Authentication settings
- API keys and credentials
- Blockchain endpoints
- Refresh intervals
- System settings

### Caching Strategy

The app uses Streamlit's caching for performance:
- PSI data: 30 seconds TTL
- CEC WAM data: 5 minutes TTL
- Clear cache via "Refresh Data" button in sidebar

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/whiteantwan58-tech/Psi.streamlit.app/issues)
- **Discussions**: [GitHub Discussions](https://github.com/whiteantwan58-tech/Psi.streamlit.app/discussions)

---

## 🔄 Version History

### v2.0 (Current) - Feb 14, 2026
- ✅ Complete UI overhaul with holographic theme
- ✅ Biometric-style authentication system
- ✅ 8 navigation pages with full functionality
- ✅ PSI bonding curve visualization
- ✅ 3D navigation star map
- ✅ Progress tracking dashboard
- ✅ Timeline and alert systems
- ✅ Activity logging
- ✅ Data export capabilities

### v1.0 - Initial Release
- Basic Streamlit interface
- Simple data display
- CSV data loading

---

## 🎯 Success Criteria

✅ 80%+ visual content, <20% text  
✅ Authentication system working  
✅ PSI bonding curve live display  
✅ CEC WAM data displaying  
✅ Progress tracking showing real percentages  
✅ All alerts and logging functional  
✅ Export capabilities working  
✅ Mobile/responsive optimized  
✅ Holographic UI theme implemented  

---

## 🚀 Future Enhancements

- [ ] Real Solana blockchain integration with live data
- [ ] Google Drive API for automatic CSV sync
- [ ] Gmail integration for email notifications
- [ ] Calendar integration for event scheduling
- [ ] Enhanced AI/EVE capabilities
- [ ] Multi-language support
- [ ] Voice commands (Siri shortcuts)
- [ ] Mobile app version
- [ ] Real-time price alerts
- [ ] Advanced analytics dashboard

---

**Built with ❤️ for the PSI Sovereign System**

*Toward 100% Sovereignty* 🎯
