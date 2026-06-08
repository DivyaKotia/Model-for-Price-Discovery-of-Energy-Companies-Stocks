# LSTM vs ARIMA — Indian Energy Sector Stock Forecasting

> **Comparing deep learning and classical time series models for predicting stock prices of Indian energy companies**

## Overview

This project develops and benchmarks an LSTM (Long Short-Term Memory) neural network against ARIMA for forecasting stock prices of Indian energy sector companies. The study covers both company-level and sub-sector-level forecasting across daily and monthly time horizons, using automated data acquisition via the Yahoo Finance API.

The core motivation: traditional time series models like ARIMA assume linearity and stationarity — assumptions that stock data routinely violates. This framework tests whether LSTM's ability to capture non-linear patterns and long-range dependencies produces meaningfully better forecasts.

---

## Key Features

- **Company-level & sub-sector-level forecasting** across daily and monthly horizons
- **Automated data pipeline** — stock data retrieved daily via `yfinance`
- **Hyperparameter tuning** using Keras Tuner's `RandomSearch`, trained separately per company
- **Overfitting controls** — dropout layers and early stopping callbacks
- **Evaluation metrics** — MSE, MAE, RMSE compared across LSTM and ARIMA

---

## Methodology

```
Data Acquisition (yfinance)
    ↓
Preprocessing & Stationarity Checks (ADF, KPSS)
    ↓
ARIMA Baseline — ACF/PACF → order selection → fit
    ↓
LSTM Model — Hyperparameter tuning (Keras Tuner RandomSearch)
         — Dropout layers + Early Stopping
    ↓
Forecast (Daily + Monthly horizons)
    ↓
Evaluation — MSE / MAE / RMSE comparison
```

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | TensorFlow / Keras, Keras Tuner |
| Time Series | statsmodels (ARIMA), Ljung-Box test |
| Data | yfinance, pandas, NumPy |
| Visualisation | Matplotlib |

---

## File Structure

```
├── Forecasting_EnergyStocksPrice.ipynb   # Main notebook: LSTM vs ARIMA comparison
├── Download_StocksData.py                # Automated data acquisition script
├── LICENSE
└── README.md
```

---

## Results Summary

LSTM outperformed ARIMA on non-stationary, non-linear price series, particularly at the daily horizon. ARIMA remained competitive for monthly aggregated data where trends are smoother. Hyperparameter tuning was company-specific — a single global model would have underfit for companies with distinct volatility regimes.

---

## Context

Developed as part of work at IIM Ahmedabad. ESG data for the same set of energy companies was analysed in a companion project ([ESG Drivers of Stock Returns](../Projects/MSc.%20Project_Forecasting%20and%20ESG%20Analysis/)).
