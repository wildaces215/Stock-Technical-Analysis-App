import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt

# Define the ticker symbol and time period
ticker_symbol = "AAPL"  # Example ticker symbol (Apple Inc.)
period = "1y"  # 1 year period

# Download historical data using Yahoo Finance API
data = yf.download(ticker_symbol, period=period)

# Calculate the Average Directional Index (ADX) using pandas-ta
data['ADX'] = ta.adx(data['High'], data['Low'], data['Close'], length=14)

# Create a figure and axis for plotting
fig, ax1 = plt.subplots()

# Plot the closing price on the primary y-axis
ax1.plot(data.index, data['Close'], label='Close', color='blue')
ax1.set_ylabel('Close Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a secondary y-axis for the ADX
ax2 = ax1.twinx()
ax2.plot(data.index, data['ADX'], label='ADX', color='red')
ax2.set_ylabel('ADX', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add a title
plt.title(f'{ticker_symbol} Price and ADX over {period}')

# Show the plot
plt.show()