import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dummy stock data
dates = pd.date_range(start='2023-01-01', periods=100)
prices = np.cumsum(np.random.randn(100)) + 100

# User interface
st.title("Stock Trading Agent")
stock_picker = st.selectbox("Choose a Stock", ['AAPL', 'GOOGL', 'MSFT'])

# Simulate moving averages
df = pd.DataFrame({'Date': dates, 'Price': prices})
df['5-day MA'] = df['Price'].rolling(window=5).mean()
df['30-day MA'] = df['Price'].rolling(window=30).mean()

# Plot
st.subheader(f"Analysis for {stock_picker}")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Date'], df['Price'], label='Price')
ax.plot(df['Date'], df['5-day MA'], label='5-day MA', linestyle='--')
ax.plot(df['Date'], df['30-day MA'], label='30-day MA', linestyle='--')
ax.legend()
ax.set_title("Stock Price and Moving Averages")
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.grid()
st.pyplot(fig)

# Recommendation
if df['5-day MA'].iloc[-1] > df['30-day MA'].iloc[-1]:
    st.success(f"Recommendation: BUY {stock_picker}")
else:
    st.error(f"Recommendation: DO NOT BUY {stock_picker}")
