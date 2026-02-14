"""
Utility functions for PSI Sovereign System
Helper functions used across the application
"""

import hashlib
import pandas as pd
import os
from datetime import datetime
from typing import Dict, List, Optional

def hash_password(password: str) -> str:
    """
    Hash password using SHA-256
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
    """
    return hashlib.sha256(password.encode()).hexdigest()

def format_currency(value: float, decimals: int = 2) -> str:
    """
    Format number as currency
    
    Args:
        value: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted currency string
    """
    return f"${value:,.{decimals}f}"

def format_percentage(value: float, decimals: int = 1) -> str:
    """
    Format number as percentage
    
    Args:
        value: Number to format
        decimals: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimals}f}%"

def get_status_color(status: str) -> str:
    """
    Get emoji color for status
    
    Args:
        status: Status string
        
    Returns:
        Emoji representing status
    """
    status_colors = {
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
    return status_colors.get(status.upper(), '⚪')

def create_log_entry(action: str, details: str, status: str, user: str = 'System') -> Dict:
    """
    Create activity log entry
    
    Args:
        action: Action performed
        details: Details of action
        status: Status of action
        user: User who performed action
        
    Returns:
        Log entry dictionary
    """
    return {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'action': action,
        'details': details,
        'status': status,
        'user': user
    }

def save_log_to_csv(log_entry: Dict, filename: str = 'activity_log.csv'):
    """
    Save log entry to CSV file
    
    Args:
        log_entry: Log entry dictionary
        filename: CSV filename to save to
    """
    try:
        df = pd.DataFrame([log_entry])
        file_exists = os.path.exists(filename)
        df.to_csv(filename, mode='a', header=not file_exists, index=False)
    except Exception as e:
        print(f"Error saving log: {e}")

def calculate_overall_progress(progress_data: Dict[str, float]) -> float:
    """
    Calculate overall progress percentage
    
    Args:
        progress_data: Dictionary of component progress percentages
        
    Returns:
        Overall progress percentage
    """
    if not progress_data:
        return 0.0
    return sum(progress_data.values()) / len(progress_data)

def format_timestamp(timestamp: datetime = None) -> str:
    """
    Format timestamp for display
    
    Args:
        timestamp: Datetime object (defaults to now)
        
    Returns:
        Formatted timestamp string
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def validate_csv_structure(df: pd.DataFrame, required_columns: List[str]) -> bool:
    """
    Validate CSV has required columns
    
    Args:
        df: DataFrame to validate
        required_columns: List of required column names
        
    Returns:
        True if valid, False otherwise
    """
    return all(col in df.columns for col in required_columns)

def generate_alert_id() -> str:
    """
    Generate unique alert ID
    
    Returns:
        Unique alert ID string
    """
    return f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

def calculate_price_change(current_price: float, previous_price: float) -> float:
    """
    Calculate percentage price change
    
    Args:
        current_price: Current price
        previous_price: Previous price
        
    Returns:
        Percentage change
    """
    if previous_price == 0:
        return 0.0
    return ((current_price - previous_price) / previous_price) * 100

def truncate_text(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """
    Truncate text to maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def format_large_number(number: float) -> str:
    """
    Format large numbers with K, M, B suffixes
    
    Args:
        number: Number to format
        
    Returns:
        Formatted number string
    """
    if number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"
    elif number >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.2f}K"
    else:
        return f"{number:.2f}"

def get_time_ago(timestamp: datetime) -> str:
    """
    Get human-readable time difference
    
    Args:
        timestamp: Past timestamp
        
    Returns:
        Time ago string (e.g., "2 hours ago")
    """
    now = datetime.now()
    diff = now - timestamp
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours ago"
    else:
        return f"{int(seconds / 86400)} days ago"
