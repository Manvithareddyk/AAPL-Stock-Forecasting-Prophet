# 📈 Time Series Forecasting of Apple (AAPL) Stock Prices using Prophet

This project demonstrates time series analysis and forecasting of Apple Inc. (AAPL) stock prices using **Facebook Prophet**. It covers the complete data pipeline from fetching real-time stock data to visualizing future trends, making it highly relevant.

---

## 🚀 Objective

To forecast AAPL stock prices by uncovering trend and seasonal components, and present a clear, data-driven financial outlook.

---
## Project Overview

This project forecasts the future stock prices of Apple Inc. (AAPL) using historical market data. It downloads stock data, processes it, and applies the **Prophet** time series forecasting model to predict future prices. The project also visualizes the forecast and its components to help understand trends and seasonal patterns in the stock price. This helps investors and analysts make more informed decisions based on predicted market behavior.

## About Prophet

[Prophet](https://facebook.github.io/prophet/) is an open-source forecasting tool developed by Facebook designed for producing high-quality forecasts for time series data. It handles seasonality, holidays, and missing data effectively, and works well with daily stock price data like Apple’s historical prices.

We chose Prophet because it provides:

- Easy-to-use API for rapid prototyping
- Robust handling of trends and seasonality without extensive manual tuning
- Strong performance on daily financial time series forecasting tasks



## 🛠️ Technologies Used

- `Python`
- `yFinance` – for historical stock data
- `Prophet` – for time series forecasting
- `Pandas`, `Matplotlib` – for data handling and visualization

---

## 📊 Project Workflow

1. **Data Collection**  
   Fetched historical AAPL stock prices (2015–2024) using `yfinance`.

2. **Data Preprocessing**  
   Cleaned and reformatted the data to match Prophet's requirements (`ds`, `y` format).

3. **Model Training with Prophet**  
   - Enabled daily seasonality
   - Set forecast horizon to 6 months
   - Handled changepoints, trends, and holidays automatically

4. **Forecast Visualization**  
   - Forecast plot with confidence intervals  
   - Trend, weekly, and yearly component plots

5. **Result Interpretation**  
   - Trends analyzed with clear visuals
   - Discussed potential future price behavior of AAPL

---

## Structure

```
AAPL-Stock-Forecasting-Prophet/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── raw_data_download.py
│   ├── processed_data.py
│   └── forecasting.py
├── README.md
├── requirements.txt
└── LICENSE
```


## 🔮 Results

- 📉 **Clear downward and upward trends** detected
- 🗓️ Weekly and yearly seasonality captured
- 📈 Accurate 6-month forecast with visual confidence bands

---

## 🧠 Insights Gained

- Understanding of stock market seasonality and trend shifts
- Hands-on experience with real-time financial data modeling
- Practical use of Prophet for interpretable forecasting

---

## How to Run

1. Run `raw_data_download.py` to download AAPL stock data.
2. Run `processed_data.py` to clean and process it.
3. Run `forecasting.py` to generate and visualize the forecast.

---
## Demo Notebook

A step-by-step demonstration of data download, processing, forecasting, and visualization using Prophet can be found in the [Jupyter Notebook here](notebooks/Time_Series_Analysis_AAPL_Prophet.ipynb).


