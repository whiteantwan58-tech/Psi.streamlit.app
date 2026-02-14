"""
API Configuration Module for Psi Crypto Dashboard

This module manages API endpoints and optional authentication.
The dashboard works completely without API keys using free public APIs.

Optional: If you want to use premium API services with higher rate limits,
you can add API keys to .streamlit/secrets.toml
"""

import streamlit as st
import os


class APIConfig:
    """
    Centralized API configuration manager.
    
    Default behavior: Uses free APIs without any authentication.
    Optional: Can read API keys from Streamlit secrets or environment variables.
    """
    
    # Free APIs that require NO authentication
    FREE_APIS = {
        'coingecko': {
            'name': 'CoinGecko',
            'base_url': 'https://api.coingecko.com/api/v3',
            'rate_limit': '50 calls/minute',
            'requires_key': False,
            'endpoints': {
                'simple_price': '/simple/price',
                'market_chart': '/coins/{coin_id}/market_chart'
            }
        },
        'coincap': {
            'name': 'CoinCap',
            'base_url': 'https://api.coincap.io/v2',
            'rate_limit': 'Unlimited (free tier)',
            'requires_key': False,
            'endpoints': {
                'assets': '/assets/{asset_id}',
                'history': '/assets/{asset_id}/history'
            }
        }
    }
    
    # Optional premium APIs (requires API keys)
    PREMIUM_APIS = {
        'cryptocompare': {
            'name': 'CryptoCompare',
            'base_url': 'https://min-api.cryptocompare.com/data',
            'requires_key': True,
            'secret_key': 'CRYPTOCOMPARE_API_KEY'
        },
        'coinmarketcap': {
            'name': 'CoinMarketCap',
            'base_url': 'https://pro-api.coinmarketcap.com/v1',
            'requires_key': True,
            'secret_key': 'COINMARKETCAP_API_KEY'
        }
    }
    
    @classmethod
    def get_api_key(cls, service_name):
        """
        Get API key for a service (optional).
        
        Returns None if no key is configured (which is fine for free APIs).
        """
        if service_name in cls.FREE_APIS:
            return None  # Free APIs don't need keys
        
        if service_name in cls.PREMIUM_APIS:
            secret_key = cls.PREMIUM_APIS[service_name]['secret_key']
            
            # Try Streamlit secrets first (safely)
            try:
                if hasattr(st, 'secrets') and secret_key in st.secrets:
                    return st.secrets[secret_key]
            except (FileNotFoundError, KeyError, AttributeError):
                # Secrets file doesn't exist or key not found - that's fine
                pass
            
            # Fall back to environment variables
            return os.getenv(secret_key)
        
        return None
    
    @classmethod
    def get_coingecko_url(cls, endpoint_type, **kwargs):
        """Get CoinGecko API URL (no authentication needed)."""
        api = cls.FREE_APIS['coingecko']
        endpoint = api['endpoints'][endpoint_type]
        
        if kwargs:
            endpoint = endpoint.format(**kwargs)
        
        return f"{api['base_url']}{endpoint}"
    
    @classmethod
    def get_coincap_url(cls, endpoint_type, **kwargs):
        """Get CoinCap API URL (no authentication needed)."""
        api = cls.FREE_APIS['coincap']
        endpoint = api['endpoints'][endpoint_type]
        
        if kwargs:
            endpoint = endpoint.format(**kwargs)
        
        return f"{api['base_url']}{endpoint}"
    
    @classmethod
    def is_using_free_apis(cls):
        """Check if only free APIs are being used (no keys configured)."""
        for service in cls.PREMIUM_APIS:
            if cls.get_api_key(service):
                return False
        return True
    
    @classmethod
    def get_status_message(cls):
        """Get a friendly status message about API configuration."""
        if cls.is_using_free_apis():
            return "🎉 Running with 100% FREE APIs - No API Keys Required!"
        else:
            active_premium = [
                name for name in cls.PREMIUM_APIS 
                if cls.get_api_key(name)
            ]
            return f"✅ Using premium APIs: {', '.join(active_premium)}"
    
    @classmethod
    def get_api_info(cls):
        """Get information about all available APIs."""
        info = []
        
        # Free APIs
        for key, api in cls.FREE_APIS.items():
            info.append({
                'name': api['name'],
                'status': '✅ Active (Free)',
                'rate_limit': api['rate_limit'],
                'requires_key': 'No'
            })
        
        # Premium APIs (if configured)
        for key, api in cls.PREMIUM_APIS.items():
            has_key = cls.get_api_key(key) is not None
            info.append({
                'name': api['name'],
                'status': '✅ Active' if has_key else '⚪ Available (requires key)',
                'rate_limit': 'Premium limits' if has_key else 'N/A',
                'requires_key': 'Yes (optional)'
            })
        
        return info


# Convenience functions for easy import
def get_coingecko_url(endpoint_type, **kwargs):
    """Get CoinGecko API URL - No API key needed."""
    return APIConfig.get_coingecko_url(endpoint_type, **kwargs)


def get_coincap_url(endpoint_type, **kwargs):
    """Get CoinCap API URL - No API key needed."""
    return APIConfig.get_coincap_url(endpoint_type, **kwargs)


def is_api_key_required():
    """Returns False - This dashboard works without any API keys."""
    return False


def get_api_status():
    """Get current API configuration status."""
    return APIConfig.get_status_message()


def get_all_api_info():
    """Get information about all available APIs."""
    return APIConfig.get_api_info()
