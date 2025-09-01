# Model-for-Price-Discovery-of-Energy-Companies-Stocks

## Overview
This repository presents a Long Short–Term Memory (LSTM) neural network–based framework for forecasting stock prices of energy companies, addressing the limitations of traditional time-series models in capturing nonlinear patterns and long-term dependencies

## Fetaures

LSTM-based forecasting can solve the issues that conventional time series models fail to address. For instance, long-term dependency, nonlinear pattern recognition, no requirement of stationarity, etc.
Some of the functionalities provided by the LSTM framework prepared for the forecasting of the stock prices of the energy companies are as discussed below:

**Company-level and sub-sector level forecasting across daily and monthly time horizons:** The framework can forecast the stock prices for individual companies as well as for aggregated sub-sectors. Also, the forecasted stock prices can be obtained for the daily data as well as for the monthly aggregated data, which enables us to understand the long-term trends as well.

**Automated data acquisition:** The data required for the forecasting is automatically retrieved daily using the Yahoo Finance API.
 
**Model optimisation and customisation:**  The model is optimised with a hyperparameter tuning process carried out using the Keras Tuner’s RandomSearch, which selects the best set of hyperparameters. Also, the model is trained separately for each company and sub-sectors, both for the daily as well as monthly data. This ensures that hyperparameter tuning is also tailored to individual company dynamics.

**Overfitting conditions:** To prevent the model from being overfit, certain steps were considered, like including dropout layers in the LSTM construction, stopping the training once the model stops learning significantly, which is executed by applying the concept of early stopping.

