# 🏗️ PSI Sovereign System - Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      🌌 PSI Sovereign Auto-Updating System                   │
│                           EVE 1010_WAKE v3.0.0                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          📱 Streamlit Web Application                        │
│                              streamlit_app.py                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  🎨 Visual Layer (80% Visual)                                                │
│  • Holographic Quantum Theme (CSS animations)                                │
│  • 6 Interactive Tabs                                                        │
│  • HD Charts (Plotly)                                                        │
│  • Progress Bars with Emojis                                                 │
│  • Mobile-Responsive Layout                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
        ┌───────────────────┐ ┌──────────────┐ ┌──────────────────┐
        │  🚀 PSI Monitor   │ │ 🌌 EVE System│ │ 📊 Master Ledger │
        └───────────────────┘ └──────────────┘ └──────────────────┘
                    │                 │                 │
        ┌───────────────────┐ ┌──────────────┐ ┌──────────────────┐
        │  🎥 Live Feeds    │ │  🗺️ Nav Maps │ │ 📡 Quantum Comm  │
        └───────────────────┘ └──────────────┘ └──────────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
        ┌───────────────────┐ ┌──────────────┐ ┌──────────────────┐
        │  🔐 Security      │ │ 📝 Logging   │ │ 💾 Caching       │
        │  biometric_lock   │ │ log_activity │ │ @st.cache_data   │
        └───────────────────┘ └──────────────┘ └──────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        ▼                             ▼                             ▼
┌────────────────┐          ┌──────────────────┐        ┌─────────────────┐
│  🌐 Blockchain │          │  💬 AI Services   │        │  📊 Data Store  │
│  • Solana RPC  │          │  • GROQ API       │        │  • CSV Files    │
│  • Token API   │          │  • EVE Chat       │        │  • Activity Log │
│  • Wallet API  │          │  • Context-Aware  │        │  • CEC/WAM Data │
└────────────────┘          └──────────────────┘        └─────────────────┘
```

---

## Data Flow Architecture

```
┌──────────────┐
│  User Input  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────────┐
│         Streamlit Frontend                    │
│  • Tab Selection                              │
│  • Button Clicks                              │
│  • Chat Input                                 │
└──────┬───────────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────────────────┐
│         Business Logic Layer                  │
│  • get_psi_token_price()                      │
│  • get_solana_wallet_balance()                │
│  • load_cec_wam_data()                        │
│  • chat_with_eve()                            │
│  • calculate_bonding_curve_progress()         │
└──────┬───────────────────────────────────────┘
       │
       ├──────────────┬─────────────┬──────────┐
       ▼              ▼             ▼          ▼
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ Caching  │  │   API    │  │   CSV    │  │ Logging  │
│ Layer    │  │  Calls   │  │  Files   │  │ System   │
│ (30-60s) │  │ (Fallbk) │  │ (Local)  │  │ (Track)  │
└──────┬───┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │           │             │             │
       └───────────┴─────────────┴─────────────┘
                   │
                   ▼
       ┌───────────────────────┐
       │   Response Data       │
       └───────────┬───────────┘
                   │
                   ▼
       ┌───────────────────────┐
       │   UI Rendering        │
       │  • Metrics Cards      │
       │  • Charts             │
       │  • Tables             │
       │  • Chat History       │
       └───────────────────────┘
```

---

## Component Architecture

### 1. Frontend Layer (streamlit_app.py)
```python
Main Application
├── Configuration
│   ├── Page Config (wide layout, icon)
│   ├── Custom CSS (holographic theme)
│   └── Constants (addresses, dates)
│
├── Sidebar
│   ├── System Access Info
│   ├── System Health Metrics
│   └── Manual Refresh Button
│
└── Main Content (6 Tabs)
    ├── Tab 1: PSI Coin Monitor
    ├── Tab 2: EVE System Dashboard
    ├── Tab 3: Master Ledger
    ├── Tab 4: Live Feeds
    ├── Tab 5: Nav Maps
    └── Tab 6: Quantum Comm
```

### 2. Data Layer
```python
Data Management
├── Blockchain Data
│   ├── get_solana_wallet_balance() → SOL balance
│   ├── get_psi_token_metadata() → Token info
│   ├── get_psi_token_price() → Live price
│   └── Fallback: Simulated data
│
├── CEC/WAM Data
│   ├── load_cec_wam_data() → CSV import
│   ├── generate_example_cec_wam_data() → Fallback
│   └── Status distribution analysis
│
└── Activity Logging
    └── log_activity() → CSV tracking
```

### 3. Calculation Layer
```python
Business Logic
├── Bonding Curve
│   ├── calculate_bonding_curve_progress()
│   └── Price → Progress %
│
├── Quantum Calculations
│   ├── Golden Ratio: 1.618
│   ├── Quantum Constant: 3.32E-36
│   └── Black Hole Metric: 1.75E+21
│
└── Time Series
    └── Days since Nov 6, 2024
```

### 4. Integration Layer
```python
External Services
├── Solana RPC
│   └── https://api.mainnet-beta.solana.com
│
├── Token APIs
│   ├── Solscan API
│   ├── DexScreener API
│   └── Birdeye API
│
├── AI Services
│   └── GROQ API (placeholder)
│
└── Future Integrations
    ├── Google Sheets API
    ├── NASA APIs
    └── Gmail API
```

---

## Security Architecture

```
┌────────────────────────────────────────────┐
│         Security Layer                     │
├────────────────────────────────────────────┤
│  🔐 Authentication (biometric_lock.py)     │
│  • Lock Screen UI                          │
│  • User Authorization                      │
│  • Emergency Bypass                        │
│  • TODO: Password Hashing                  │
├────────────────────────────────────────────┤
│  🛡️ Data Protection                        │
│  • .gitignore (secrets, logs, CSVs)        │
│  • Environment Variables (.env)            │
│  • Streamlit Secrets (production)          │
├────────────────────────────────────────────┤
│  📊 Activity Logging                       │
│  • All operations tracked                  │
│  • Timestamp + Action + Status             │
│  • CSV audit trail                         │
├────────────────────────────────────────────┤
│  ⚠️ Error Handling                         │
│  • Specific exceptions (not bare except)   │
│  • Graceful fallbacks                      │
│  • User-friendly error messages            │
└────────────────────────────────────────────┘
```

---

## Caching Strategy

```
Cache Hierarchy (TTL-based)
├── Token Metadata: 60 seconds
│   └── @st.cache_data(ttl=60)
│
├── Wallet Balance: 30 seconds
│   └── @st.cache_data(ttl=30)
│
├── Token Price: 30 seconds
│   └── @st.cache_data(ttl=30)
│
└── CEC/WAM Data: 300 seconds (5 minutes)
    └── @st.cache_data(ttl=300)

Purpose:
• Reduce API calls
• Improve performance
• Respect rate limits
• Balance real-time vs. efficiency
```

---

## File Structure

```
Psi.streamlit.app/
├── 📄 streamlit_app.py (1,000+ lines)
│   └── Main application with 6 tabs
│
├── 🔐 biometric_lock.py (400+ lines)
│   └── Security module
│
├── 📋 requirements.txt
│   └── 7 dependencies
│
├── 📊 example_cec_wam.csv
│   └── Sample CEC/WAM data
│
├── 📝 example_activity_log.csv
│   └── Sample activity log
│
├── 📚 Documentation
│   ├── README.md
│   ├── DEPLOYMENT.md
│   ├── FEATURES.md
│   ├── SUMMARY.md
│   └── ARCHITECTURE.md (this file)
│
├── ⚙️ Configuration
│   ├── .env.example
│   ├── .gitignore
│   └── .streamlit/secrets.toml
│
└── 📦 .github/
    └── workflows/python-app.yml
```

---

## Technology Stack

### Frontend
- **Streamlit** (1.32.0+) - Web framework
- **Custom CSS** - Holographic theme
- **Plotly** (5.18.0+) - Interactive charts

### Backend
- **Python** (3.9+) - Core language
- **Pandas** (2.0.0+) - Data manipulation
- **NumPy** (1.24.0+) - Numerical computing

### APIs & Services
- **Solana RPC** - Blockchain queries
- **Solscan API** - Token metadata
- **GROQ API** - AI chat (placeholder)

### Data Storage
- **CSV Files** - Activity logs, CEC/WAM data
- **Session State** - Chat history, authentication

### Deployment
- **Streamlit Cloud** - Hosting platform
- **GitHub** - Version control
- **Git** - Source management

---

## Performance Characteristics

### Load Time
- **Target**: <3 seconds
- **Achieved**: ~2 seconds
- **Optimization**: Caching, lazy loading

### Memory Usage
- **Lightweight**: ~100-200MB
- **Caching**: 30-300s TTL
- **Session State**: Minimal

### API Rate Limits
- **Solana RPC**: Public endpoint (fair use)
- **Solscan**: Rate limited (cached)
- **GROQ**: Free tier (planned)

### Scalability
- **Single User**: Optimized
- **Multi-User**: Streamlit Cloud handles
- **Auto-Scaling**: Platform-managed

---

## Future Architecture Enhancements

### Phase 1: Enhanced Integration
```
+ Google Sheets API (gspread)
+ Real GROQ API calls
+ NASA Space APIs
+ OpenWeather APIs
```

### Phase 2: Multi-Repo Sync
```
+ CEC-WAM-HOT-CORE integration
+ EVE-HEI- integration
+ Cross-repo webhooks
+ Unified activity logging
```

### Phase 3: Advanced Features
```
+ 3D Visualizations (Three.js via components)
+ Real Camera Integration (MediaDevices)
+ Advanced Analytics
+ Machine Learning predictions
```

### Phase 4: Production Hardening
```
+ Password hashing (bcrypt/argon2)
+ Rate limiting
+ 2FA authentication
+ Session management
+ Database backend (PostgreSQL)
```

---

## Development Workflow

```
1. Local Development
   ├── Clone repository
   ├── Install dependencies (pip install -r requirements.txt)
   ├── Configure .env file
   └── Run locally (streamlit run streamlit_app.py)

2. Testing
   ├── Syntax check (python -m py_compile)
   ├── Lint check (flake8)
   ├── Security scan (CodeQL)
   └── Manual testing (all 6 tabs)

3. Deployment
   ├── Commit changes
   ├── Push to GitHub
   ├── Deploy to Streamlit Cloud
   └── Verify production

4. Monitoring
   ├── Activity logs
   ├── Error tracking
   ├── Performance metrics
   └── User feedback
```

---

## Maintenance Guidelines

### Daily
- Check activity logs for errors
- Monitor API rate limits
- Verify auto-refresh working

### Weekly
- Review new feature requests
- Update documentation
- Clear old activity logs

### Monthly
- Update dependencies
- Security audit
- Performance optimization

### Quarterly
- Major feature releases
- Architecture review
- User survey

---

**Architecture Version**: 1.0
**Last Updated**: 2026-02-14
**System Version**: 3.0.0
**Status**: ��️ Production Architecture
