# Copilot Instructions for PSI-Coin Streamlit App

## Repository Context

This is a Streamlit-based web application for real-time Solana blockchain monitoring, specifically designed to track PSI-Coin (EVE 1010_WAKE). The application provides live data tracking, wallet balance monitoring, and a CEC/WAM (Wide Area Monitoring) system that integrates with Google Sheets.

### Key Components

- **Main Application**: `streamlit_app.py` - Single-file Streamlit application
- **Blockchain Integration**: Solana mainnet-beta RPC connection
- **External APIs**: Solscan API for token metadata and pricing
- **Data Sources**: Google Sheets (for CEC/WAM live data)
- **Python Version**: 3.8+

## Architecture and Design Patterns

### Application Structure

- Single-file architecture using `streamlit_app.py`
- Tab-based UI with 5 main sections:
  1. Live Data (blockchain metrics)
  2. CEC/WAM Live (Google Sheets integration)
  3. Holdings (portfolio calculator)
  4. CSV Data (file management)
  5. About (documentation)

### Caching Strategy

- Use Streamlit's `@st.cache_data` decorator for API calls
- Token metadata: 60-second TTL
- Wallet balance: 30-second TTL
- CEC/WAM data: 300-second (5-minute) TTL
- Always include proper error handling in cached functions

## Code Standards

### Python Style

- Follow PEP 8 style guidelines
- Maximum line length: 127 characters (per existing flake8 config)
- Use descriptive variable names
- Add docstrings to all functions
- Use type hints where appropriate

### Function Design

```python
@st.cache_data(ttl=60)
def fetch_data(param):
    """Fetch data from external API
    
    Args:
        param: Description of parameter
        
    Returns:
        Data object or None on failure
    """
    try:
        # Implementation
        return result
    except Exception as e:
        st.error(f"Error: {e}")
        return None
```

### Error Handling

- **ALWAYS** use try-except blocks for external API calls
- Use appropriate Streamlit message functions:
  - `st.error()` for errors
  - `st.warning()` for warnings
  - `st.info()` for informational messages
  - `st.success()` for success messages
- Provide graceful fallbacks (e.g., return 0.0 instead of crashing)
- Include descriptive error messages that help users understand what went wrong

### Dashboard and UI Guidelines

1. **Auto-Display Dashboard**: The app should automatically display the dashboard on load without requiring user interaction
2. **Link Verification**: All external links (Solscan, Google Sheets, blockchain explorers) must be tested and valid
3. **Error Link Checking**: When errors occur, ensure error messages include links to documentation or help resources when applicable
4. **Data Freshness Indicators**: Always show timestamps for when data was last updated
5. **Loading States**: Use `st.spinner()` for all data fetching operations
6. **Responsive Layout**: Use `st.columns()` for side-by-side metrics and data

## Security Best Practices

### Environment Variables

- **NEVER** hardcode API keys or secrets in source code
- Use `os.getenv()` to load sensitive configuration
- Add all sensitive files to `.gitignore`
- Document required environment variables in README

### Allowed in Code

- Public blockchain addresses (read-only)
- Public API endpoints
- Configuration that doesn't expose sensitive data

### Not Allowed in Code

- Private keys or secrets
- Personal API keys
- Database credentials
- User data

## Testing Requirements

### Before Making Changes

1. Run existing linters: `flake8 . --count --select=E9,F63,F7,F82`
2. Check for syntax errors and undefined names
3. Test affected functionality manually

### After Making Changes

1. Run linters again to ensure no new issues
2. Test the Streamlit app locally: `streamlit run streamlit_app.py`
3. Verify all tabs load correctly
4. Check that auto-refresh works (if enabled)
5. Verify external API calls work correctly
6. Test error handling by simulating failures

### No Unit Tests

- This repository does not currently have pytest unit tests
- The CI workflow expects pytest but no tests are present
- Manual testing through the UI is the primary validation method
- Do not add pytest tests unless specifically requested

## CEC/WAM System

### Purpose

The CEC/WAM (Wide Area Monitoring) system provides real-time data synchronization from Google Sheets with color-coded status indicators.

### Status Codes

- 🟢 **PERFECT**: System operating optimally
- 🟡 **TODO**: Items requiring attention
- 🔵 **ACTIVE**: Currently processing or in progress
- ⚪ **STABLE**: System in stable state

### Implementation Requirements

1. Data must auto-refresh every 5 minutes (300 seconds)
2. Status column is required for color-coding
3. Google Sheet must be publicly accessible
4. Use CSV export URL format for data fetching
5. Display status distribution analytics
6. Provide data export functionality

### Error Handling for CEC/WAM

- Check if `CEC_WAM_SHEET_URL` is configured before attempting to fetch
- Validate Google Sheets URL format
- Handle empty sheets gracefully
- Provide clear error messages for common issues (permissions, invalid URL, etc.)

## Common Modifications

### Adding New Metrics

1. Create a cached function with appropriate TTL
2. Add error handling
3. Display using `st.metric()` or appropriate Streamlit component
4. Include loading spinner
5. Add to appropriate tab in the UI

### Adding New API Integration

1. Add API endpoint constants at the top of the file
2. Create cached function with `@st.cache_data(ttl=X)`
3. Use requests with timeout parameter (10-15 seconds)
4. Handle errors gracefully with try-except
5. Return None or default values on failure
6. Update documentation in README

### Adding New Configuration

1. Define constant at the top of the file
2. Load from environment variable using `os.getenv()`
3. Provide sensible defaults
4. Document in README under Setup Instructions
5. Add to Streamlit Cloud secrets documentation if sensitive

## Streamlit-Specific Guidelines

### State Management

- Use `st.session_state` for persistent state across reruns
- Initialize session state variables before use
- Be careful with auto-refresh and state persistence

### Performance

- Cache expensive operations (API calls, data processing)
- Use `use_container_width=True` for dataframes
- Limit data display size (use pagination or limits)
- Set appropriate heights for large dataframes

### UI Components

- Use `st.tabs()` for organizing different views
- Use `st.columns()` for side-by-side layout
- Use `st.expander()` for collapsible sections
- Use `st.divider()` to separate sections
- Use `st.caption()` for metadata and timestamps

## Deployment

### Streamlit Cloud

- Application is deployed on Streamlit Cloud
- Secrets are managed through Streamlit Cloud Secrets (TOML format)
- No `.env` file in production
- Public Google Sheets required for CEC/WAM

### CI/CD

- GitHub Actions workflow runs on push and PR to main branch
- Linting with flake8 is required
- Pytest runs but no tests currently exist (will pass)
- All syntax errors must be fixed before merge

## Common Issues and Solutions

### API Rate Limiting

- Implement caching with appropriate TTL
- Add delays between requests if needed
- Handle 429 status codes gracefully

### Auto-Refresh Issues

- Auto-refresh causes full page rerun
- Be mindful of expensive operations
- Use caching to minimize API calls
- Ensure state is preserved across reruns

### Google Sheets Integration

- Sheet must be publicly accessible ("Anyone with link can view")
- Use CSV export URL format
- Handle connection timeouts (15 seconds timeout)
- Validate sheet contains expected columns

## When to Ask for Clarification

- Adding new external dependencies (requires testing for security vulnerabilities)
- Changing core architecture or file structure
- Implementing authentication or user data storage
- Adding database connections
- Changing blockchain addresses or network configurations

## Work Verification Checklist

Before completing any task:

1. ✅ All errors are fixed and handled gracefully
2. ✅ All links are tested and working correctly
3. ✅ Dashboard displays automatically on load
4. ✅ Auto-refresh works if enabled
5. ✅ External API calls have proper error handling
6. ✅ Linting passes (flake8)
7. ✅ Manual testing completed in local environment
8. ✅ No hardcoded secrets or sensitive data
9. ✅ Documentation updated if needed
10. ✅ Code follows existing patterns and style
