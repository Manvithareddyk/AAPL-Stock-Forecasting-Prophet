import pandas as pd

# Load the raw data
data = pd.read_csv('data/raw/AAPL_raw.csv')

# Select and rename required columns for Prophet
df = data[['Date', 'Close']].copy()
df.columns = ['ds', 'y']

# Save processed data
df.to_csv('data/processed/AAPL_processed.csv', index=False)
print("Processed data saved to data/processed/AAPL_processed.csv")
