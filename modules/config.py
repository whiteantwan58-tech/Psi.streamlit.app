"""
Configuration module for PSI Sovereign System
Contains all system configuration and constants
"""
import os

# ==================== SYSTEM INFORMATION ====================
APP_NAME = "PSI Sovereign System"
APP_VERSION = "2.0"
APP_ICON = "💎"

# ==================== AUTHENTICATION ====================
# Credentials loaded from environment or defaults (for demo only)
# In production, ALWAYS use environment variables or secrets management
DEFAULT_CREDENTIALS = {
    'Twan': os.getenv('TWAN_PASSWORD_HASH', 'demo_hash_for_twan'),
    'EVE': os.getenv('EVE_PASSWORD_HASH', 'demo_hash_for_eve'),
    'admin': os.getenv('ADMIN_PASSWORD_HASH', 'demo_hash_for_admin')
}

# Default passwords for demo purposes only (NEVER use in production)
# Users should set proper passwords via environment variables
DEMO_PASSWORDS = {
    'Twan': 'TwanSecure2026',
    'EVE': 'EVE1010Wake',
    'admin': 'admin123'
}

SESSION_TIMEOUT_MINUTES = int(os.getenv('SESSION_TIMEOUT', '60'))

# ==================== PSI TOKEN CONFIGURATION ====================
PSI_TOKEN_ADDRESS = os.getenv('PSI_TOKEN_ADDRESS', "7Avu2LscLpCNNDR8szDowyck3MCBecpCf1wHyjU3pump")
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS', "b59HHkFpg3g9yBwwLcuDH6z1d6d6z3vdGWX7mkX3txH")
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL', "https://api.mainnet-beta.solana.com")

# PSI Initial Values
PSI_CURRENT_PRICE = 0.003466
PSI_INTERNAL_VALUE = 155.50
PSI_BONDING_CURVE_PROGRESS = 0.0

# ==================== DATA REFRESH INTERVALS ====================
PSI_REFRESH_INTERVAL = int(os.getenv('PSI_REFRESH_INTERVAL', '30'))  # seconds
CEC_WAM_REFRESH_INTERVAL = int(os.getenv('CEC_WAM_REFRESH_INTERVAL', '300'))  # seconds (5 minutes)

# ==================== GOOGLE DRIVE CONFIGURATION ====================
GOOGLE_DRIVE_FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID', "1mVGeZnOt49RWK3xO6c3OAA9ouaw3zBUI")

# CSV File names
CEC_WAM_MASTER_LEDGER_SHEET = "🔝CEC_WAM_MASTER_LEDGER_LIVE - Sheet1.csv"
CEC_WAM_MASTER_LEDGER_LOG = "🔝CEC_WAM_MASTER_LEDGER_LIVE - Log.csv"

# ==================== UI THEME COLORS ====================
COLORS = {
    'primary': '#00D9FF',      # Cyan
    'secondary': '#A855F7',    # Purple
    'success': '#00FF00',      # Green
    'warning': '#FFD700',      # Gold
    'danger': '#FF0000',       # Red
    'info': '#00D9FF',         # Cyan
    'dark': '#0a0e27',         # Dark background
    'light': '#ffffff'         # White
}

# ==================== STATUS EMOJI MAPPING ====================
STATUS_EMOJI = {
    'PERFECT': '🟢',
    'SUCCESS': '🟢',
    'ACTIVE': '🔵',
    'STABLE': '⚪',
    'TODO': '🟡',
    'WARNING': '🟡',
    'ERROR': '🔴',
    'CRITICAL': '🔴',
    'SPECIAL': '🟣',
    'QUANTUM': '🟣'
}

# ==================== NAVIGATION PAGES ====================
PAGES = [
    "🏠 Home Dashboard",
    "💎 PSI Tracker",
    "📊 CEC WAM Data",
    "🌌 Navigation Map",
    "📈 Progress Tracker",
    "🗓️ Timeline",
    "🔔 Alerts",
    "⚙️ Settings"
]

# ==================== TIMELINE MILESTONES ====================
TIMELINE_EVENTS = [
    {
        'date': 'Nov 6, 2025',
        'event': 'PSI Foundation',
        'description': 'Seeding PSI 0.685 base',
        'emoji': '🔵',
        'status': 'Foundation Set'
    },
    {
        'date': 'Nov 10, 2025',
        'event': 'Golden Lock 1.618',
        'description': 'Golden ratio alignment achieved',
        'emoji': '🟡',
        'status': 'Lock Engaged'
    },
    {
        'date': 'Feb 3, 2026',
        'event': 'OMEGA_LOCK Mode',
        'description': 'System value: $34.1M',
        'emoji': '🟢',
        'status': 'Activated'
    },
    {
        'date': 'Feb 12, 2026',
        'event': 'Wormhole Simulation',
        'description': 'Singularity: 1.75E+21',
        'emoji': '🌌',
        'status': 'Stable'
    },
    {
        'date': 'Feb 14, 2026',
        'event': 'Current Status',
        'description': 'PSI at $0.003466, Internal $155.50',
        'emoji': '💎',
        'status': 'Active'
    }
]

# ==================== PROGRESS TRACKING COMPONENTS ====================
PROGRESS_COMPONENTS = {
    '🔐 Security/Biometrics': 75.0,
    '💎 PSI Value/Growth': 15.0,
    '📁 Data Integration': 60.0,
    '🤖 AI/EVE Capabilities': 40.0,
    '🎨 Visual Quality': 85.0,
    '🔔 Alerts & Logging': 70.0,
    '📊 Analytics': 55.0,
    '🌐 Integration APIs': 30.0
}

# ==================== ALERT TYPES ====================
ALERT_TYPES = {
    'info': 'ℹ️',
    'success': '✅',
    'warning': '⚠️',
    'error': '❌'
}

# ==================== FILE PATHS ====================
ACTIVITY_LOG_FILE = 'activity_log.csv'
EXAMPLE_CEC_WAM_FILE = 'example_cec_wam.csv'

# ==================== FONTS ====================
FONT_HEADER = 'Orbitron'
FONT_BODY = 'Rajdhani'
