import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('data/processed/AAPL_cleaned.csv')

# Convert date column again just to be sure
df['ds'] = pd.to_datetime(df['ds'])

# Initialize and train the model
model = Prophet(daily_seasonality=True)
model.fit(df)

# Forecasting
future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

# Plot the forecast
model.plot(forecast)
plt.title('AAPL Stock Price Forecast')
plt.show()

# Plot components
model.plot_components(forecast)
plt.show()
