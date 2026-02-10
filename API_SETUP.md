# 🔓 API Configuration Guide

## ✅ No API Keys Required!

The **Psi Crypto Dashboard** works completely **FREE** without any API keys or authentication. You can start using it immediately after deployment with zero configuration.

## 🆓 Free APIs Used

### 1. CoinGecko API (Primary)
- **Authentication**: None required ✅
- **Rate Limit**: 50 calls/minute (free tier)
- **Features**: Real-time prices, market caps, 24h changes, historical data
- **Documentation**: https://www.coingecko.com/en/api

### 2. CoinCap API (Backup)
- **Authentication**: None required ✅
- **Rate Limit**: Unlimited (free tier)
- **Features**: Real-time crypto prices, historical data
- **Documentation**: https://docs.coincap.io/

## 🚀 Quick Start (No Configuration Needed)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app - IT JUST WORKS!
streamlit run streamlit_app.py
```

That's it! No API keys, no configuration files, no setup required.

## 🎛️ Optional: Premium API Support (Future)

If you want to use premium APIs with higher rate limits in the future, you can optionally configure API keys.

### Step 1: Create Secrets File

Copy the example file:
```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

### Step 2: Add Your API Keys

Edit `.streamlit/secrets.toml` and add your keys:

```toml
# Optional premium API keys
CRYPTOCOMPARE_API_KEY = "your_key_here"
COINMARKETCAP_API_KEY = "your_key_here"
```

### Step 3: Deploy to Streamlit Cloud

When deploying to Streamlit Cloud, add secrets through the dashboard:
1. Go to your app settings
2. Click on "Secrets"
3. Paste your secrets in TOML format
4. Save

**Note**: Premium APIs are not currently implemented. The app works perfectly with free APIs!

## 📊 API Status Check

The dashboard includes an API configuration module that shows:
- Which APIs are active
- Whether API keys are configured
- Current rate limits
- Status of all data sources

Import and use it:

```python
from api_config import get_api_status, get_all_api_info

# Check current status
status = get_api_status()
print(status)  # "🎉 Running with 100% FREE APIs - No API Keys Required!"

# Get detailed info
api_info = get_all_api_info()
for api in api_info:
    print(f"{api['name']}: {api['status']}")
```

## 🔐 Security Best Practices

Even though this app doesn't require API keys, here are security best practices:

### ✅ What's Already Protected
- `.streamlit/secrets.toml` is in `.gitignore`
- `.env` files are ignored
- No API keys in source code
- No credentials in configuration files

### 🛡️ If You Add Premium APIs
- Never commit `.streamlit/secrets.toml` to Git
- Use environment variables in production
- Rotate API keys regularly
- Monitor API usage for anomalies
- Use Streamlit Cloud secrets manager for deployment

## 🆘 Troubleshooting

### Issue: "API rate limit exceeded"
**Solution**: The free APIs have rate limits:
- **CoinGecko**: 50 calls/minute
- **App caching**: 5-10 minutes TTL reduces calls

The app automatically uses caching to stay within limits.

### Issue: "Failed to fetch data"
**Solution**: The app has automatic fallback:
1. Tries CoinGecko API first
2. Falls back to cached data
3. Can use CoinCap API as backup

Check your internet connection and firewall settings.

### Issue: "Where do I add API keys?"
**Answer**: You don't need any! The app works without API keys.

If you really want to add optional premium keys in the future:
1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml`
2. Add your keys there
3. Restart the app

## 🌟 Adding More Free APIs

Want to add another free cryptocurrency API? Here's how:

### 1. Update `api_config.py`

Add your API to the `FREE_APIS` dictionary:

```python
FREE_APIS = {
    'your_api': {
        'name': 'Your API Name',
        'base_url': 'https://api.example.com',
        'rate_limit': '100 calls/minute',
        'requires_key': False,
        'endpoints': {
            'prices': '/prices',
            'historical': '/history'
        }
    }
}
```

### 2. Create Helper Functions

```python
def fetch_from_your_api():
    url = APIConfig.get_your_api_url('prices')
    response = requests.get(url, timeout=10)
    return response.json()
```

### 3. Update Data Fetching

Modify your page files to use the new API as needed.

## 📚 Resources

- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [CoinGecko API Docs](https://www.coingecko.com/en/api/documentation)
- [CoinCap API Docs](https://docs.coincap.io/)
- [Streamlit Configuration](https://docs.streamlit.io/library/advanced-features/configuration)

## 💡 Summary

**TL;DR**: 
- ✅ No API keys required
- ✅ Works immediately after installation
- ✅ 100% free forever
- ✅ Optional premium API support for future
- ✅ Secure by default
- ✅ Easy to extend with more APIs

Just run `streamlit run streamlit_app.py` and enjoy! 🚀
