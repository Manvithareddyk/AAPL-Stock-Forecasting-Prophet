import yfinance as yf
import pandas as pd

# Download Apple stock data
data = yf.download('AAPL', start='2015-01-01', end='2024-12-31')

# Reset index to make 'Date' a column
data.reset_index(inplace=True)

# Save raw data to CSV
data.to_csv('data/raw/AAPL_raw.csv', index=False)
print("Raw data saved to data/raw/AAPL_raw.csv")
