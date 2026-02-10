import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Portfolio Tracker - Psi Crypto",
    page_icon="💼",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        }
        .stApp {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        }
        h1 {
            color: #00f5ff;
        }
        h2, h3 {
            color: #ffffff;
        }
        .portfolio-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            backdrop-filter: blur(10px);
            margin: 10px 0;
        }
        .profit {
            color: #00ff88;
            font-weight: bold;
        }
        .loss {
            color: #ff4444;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Data fetching
@st.cache_data(ttl=300)
def fetch_current_prices():
    """Fetch current prices for cryptocurrencies"""
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "bitcoin,ethereum,solana",
                "vs_currencies": "usd"
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return {
            'bitcoin': data['bitcoin']['usd'],
            'ethereum': data['ethereum']['usd'],
            'solana': data['solana']['usd']
        }
    except:
        # Fallback prices
        return {
            'bitcoin': 94500,
            'ethereum': 3200,
            'solana': 145
        }

# Initialize session state for portfolio
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = []

# Header
st.title("💼 Portfolio Tracker")
st.markdown("Track your cryptocurrency holdings and performance")

# Fetch current prices
current_prices = fetch_current_prices()

coin_display_map = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'solana': 'Solana (SOL)'
}

# Add holding section
st.markdown("---")
st.markdown("## ➕ Add Holding")

col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_coin = st.selectbox(
        "Cryptocurrency",
        options=list(coin_display_map.keys()),
        format_func=lambda x: coin_display_map[x]
    )

with col2:
    amount = st.number_input("Amount", min_value=0.0, value=0.0, step=0.01, format="%.4f")

with col3:
    purchase_price = st.number_input(
        "Purchase Price ($)",
        min_value=0.0,
        value=current_prices[selected_coin],
        step=0.01,
        format="%.2f"
    )

with col4:
    st.markdown("&nbsp;")
    if st.button("➕ Add to Portfolio", use_container_width=True):
        if amount > 0:
            st.session_state.portfolio.append({
                'coin': selected_coin,
                'amount': amount,
                'purchase_price': purchase_price,
                'purchase_value': amount * purchase_price
            })
            st.success(f"Added {amount} {coin_display_map[selected_coin]} to portfolio!")
            st.rerun()
        else:
            st.error("Please enter a valid amount")

# Display portfolio
st.markdown("---")
st.markdown("## 📊 Your Portfolio")

if len(st.session_state.portfolio) == 0:
    st.info("👋 Your portfolio is empty. Add your first holding above to get started!")
else:
    # Calculate portfolio metrics
    portfolio_data = []
    total_value = 0
    total_investment = 0
    
    for idx, holding in enumerate(st.session_state.portfolio):
        coin = holding['coin']
        amount = holding['amount']
        purchase_price = holding['purchase_price']
        purchase_value = holding['purchase_value']
        
        current_price = current_prices[coin]
        current_value = amount * current_price
        profit_loss = current_value - purchase_value
        profit_loss_pct = (profit_loss / purchase_value) * 100 if purchase_value > 0 else 0
        
        portfolio_data.append({
            'index': idx,
            'Coin': coin_display_map[coin],
            'Amount': amount,
            'Purchase Price': purchase_price,
            'Current Price': current_price,
            'Investment': purchase_value,
            'Current Value': current_value,
            'Profit/Loss': profit_loss,
            'P/L %': profit_loss_pct
        })
        
        total_value += current_value
        total_investment += purchase_value
    
    df = pd.DataFrame(portfolio_data)
    
    # Portfolio summary metrics
    total_profit_loss = total_value - total_investment
    total_profit_loss_pct = (total_profit_loss / total_investment) * 100 if total_investment > 0 else 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Investment", f"${total_investment:,.2f}")
    
    with col2:
        st.metric("Current Value", f"${total_value:,.2f}")
    
    with col3:
        st.metric(
            "Total Profit/Loss",
            f"${total_profit_loss:,.2f}",
            f"{total_profit_loss_pct:.2f}%",
            delta_color="normal" if total_profit_loss >= 0 else "inverse"
        )
    
    with col4:
        if total_profit_loss >= 0:
            st.success(f"📈 Portfolio Up {total_profit_loss_pct:.2f}%")
        else:
            st.error(f"📉 Portfolio Down {abs(total_profit_loss_pct):.2f}%")
    
    # Portfolio table
    st.markdown("---")
    st.markdown("### 📋 Holdings Details")
    
    # Format display dataframe
    display_df = df[['Coin', 'Amount', 'Purchase Price', 'Current Price', 'Investment', 'Current Value', 'Profit/Loss', 'P/L %']].copy()
    
    # Format columns
    for col in ['Purchase Price', 'Current Price', 'Investment', 'Current Value', 'Profit/Loss']:
        display_df[col] = display_df[col].apply(lambda x: f"${x:,.2f}")
    
    display_df['P/L %'] = display_df['P/L %'].apply(lambda x: f"{x:.2f}%")
    display_df['Amount'] = display_df['Amount'].apply(lambda x: f"{x:.4f}")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    # Portfolio allocation pie chart
    st.markdown("---")
    st.markdown("### 🥧 Portfolio Allocation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # By current value
        allocation_df = df.groupby('Coin')['Current Value'].sum().reset_index()
        
        fig_allocation = px.pie(
            allocation_df,
            values='Current Value',
            names='Coin',
            title='Allocation by Current Value',
            color_discrete_sequence=['#00f5ff', '#00ff88', '#ff4444']
        )
        
        fig_allocation.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            height=400
        )
        
        st.plotly_chart(fig_allocation, use_container_width=True)
    
    with col2:
        # Performance by coin
        performance_df = df.groupby('Coin').agg({
            'Profit/Loss': 'sum',
            'P/L %': 'mean'
        }).reset_index()
        
        fig_performance = go.Figure()
        
        colors = ['#00ff88' if x >= 0 else '#ff4444' for x in performance_df['Profit/Loss']]
        
        fig_performance.add_trace(go.Bar(
            x=performance_df['Coin'],
            y=performance_df['Profit/Loss'],
            marker_color=colors,
            text=[f"${x:,.2f}" for x in performance_df['Profit/Loss']],
            textposition='outside'
        ))
        
        fig_performance.update_layout(
            title='Profit/Loss by Asset',
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis_title='Asset',
            yaxis_title='Profit/Loss (USD)',
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig_performance, use_container_width=True)
    
    # Performance metrics
    st.markdown("---")
    st.markdown("### 📈 Performance Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        best_performer = df.loc[df['P/L %'].idxmax()]
        st.markdown(f"""
        <div class="portfolio-card">
            <h4>🏆 Best Performer</h4>
            <p><strong>{best_performer['Coin']}</strong></p>
            <p class="profit">+{best_performer['P/L %']:.2f}%</p>
            <p>${best_performer['Profit/Loss']:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        worst_performer = df.loc[df['P/L %'].idxmin()]
        st.markdown(f"""
        <div class="portfolio-card">
            <h4>📉 Worst Performer</h4>
            <p><strong>{worst_performer['Coin']}</strong></p>
            <p class="loss">{worst_performer['P/L %']:.2f}%</p>
            <p>${worst_performer['Profit/Loss']:.2f}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        largest_holding = df.loc[df['Current Value'].idxmax()]
        st.markdown(f"""
        <div class="portfolio-card">
            <h4>💎 Largest Holding</h4>
            <p><strong>{largest_holding['Coin']}</strong></p>
            <p>${largest_holding['Current Value']:.2f}</p>
            <p>{(largest_holding['Current Value'] / total_value * 100):.1f}% of portfolio</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Manage portfolio
    st.markdown("---")
    st.markdown("### ⚙️ Manage Portfolio")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if len(st.session_state.portfolio) > 0:
            remove_index = st.selectbox(
                "Select holding to remove",
                options=range(len(st.session_state.portfolio)),
                format_func=lambda x: f"{coin_display_map[st.session_state.portfolio[x]['coin']]} - {st.session_state.portfolio[x]['amount']:.4f} coins"
            )
    
    with col2:
        st.markdown("&nbsp;")
        if st.button("🗑️ Remove Selected", use_container_width=True):
            if len(st.session_state.portfolio) > 0:
                removed = st.session_state.portfolio.pop(remove_index)
                st.success(f"Removed {coin_display_map[removed['coin']]} from portfolio")
                st.rerun()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Refresh Prices", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
    
    with col2:
        if st.button("🗑️ Clear All Holdings", use_container_width=True):
            st.session_state.portfolio = []
            st.success("Portfolio cleared!")
            st.rerun()

# Tips section
st.markdown("---")
with st.expander("💡 Portfolio Tips"):
    st.markdown("""
    ### How to use the Portfolio Tracker
    
    1. **Add Holdings**: Enter the amount and purchase price of your cryptocurrencies
    2. **Track Performance**: Monitor your profit/loss in real-time
    3. **View Allocation**: See how your portfolio is distributed across assets
    4. **Manage**: Remove individual holdings or clear entire portfolio
    
    ### Important Notes
    
    - 📊 Portfolio data is stored in your browser session
    - 🔄 Prices update automatically when you refresh
    - 💾 Data is not persisted between sessions
    - 📱 Works across all devices
    
    ### Risk Management
    
    - Diversify across multiple assets
    - Set stop-loss levels
    - Don't invest more than you can afford to lose
    - Regular rebalancing recommended
    """)

# Footer
st.markdown("---")
st.caption("💡 Prices updated every 5 minutes | Portfolio stored locally | Not financial advice")
