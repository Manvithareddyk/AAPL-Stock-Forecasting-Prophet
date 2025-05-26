import pandas as pd

# Load processed data
df = pd.read_csv('data/processed/AAPL_processed.csv')

# Convert columns to correct types
df['ds'] = pd.to_datetime(df['ds'])
df['y'] = pd.to_numeric(df['y'], errors='coerce')
df.dropna(inplace=True)

# Save the cleaned data again (optional)
df.to_csv('data/processed/AAPL_cleaned.csv', index=False)
print("Cleaned data saved to data/processed/AAPL_cleaned.csv")
