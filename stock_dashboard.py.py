import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Set up page title
st.set_page_config(page_title="Stock Market Dashboard", layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, GOOGL, MSFT)", "AAPL").upper()

# Date range selection
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2026-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

if ticker_symbol:
    try:
        with st.spinner("Fetching stock data..."):
            # Fetch data and clean up columns instantly
            df = yf.download(ticker_symbol, start=start_date, end=end_date)
            
        if not df.empty:
            # Flatten multi-index columns if present
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.droplevel(1)
                
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader(f"Current Metrics for {ticker_symbol}")
                
                # Fetch the last row value safely as a plain number
                latest_price = float(df['Close'].values[-1])
                st.metric(label="Latest Closing Price", value=f"${latest_price:.2f}")
                st.dataframe(df.tail(10))
            
            with col2:
                st.subheader("Price History & Financial Chart")
                # Create interactive chart safely
                fig = go.Figure(data=[go.Candlestick(
                    x=df.index,
                    open=df['Open'].values,
                    high=df['High'].values,
                    low=df['Low'].values,
                    close=df['Close'].values,
                    name=ticker_symbol
                )])
                fig.update_layout(xaxis_rangeslider_visible=True, template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("No data found for this ticker symbol. Please check the spelling.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
