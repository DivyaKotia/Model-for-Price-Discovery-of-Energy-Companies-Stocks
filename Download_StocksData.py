
# from google.colab import drive
# drive.mount('/content/drive')

import pandas as pd
import yfinance as yf
from datetime import datetime
import numpy as np
import os

# os.chdir('/content/drive/MyDrive/IIMA_Internship/Energy_Sector')

stock_data = {}
industry_data = {}
Month_df = {}
Month_df_industry = {}
Results = {}

# List of stock symbols
stocks_list = ['IOC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'NTPC.NS', 'COALINDIA.NS',
          'ONGC.NS', 'BPCL.NS', 'ADANIPOWER.NS', 'TATAPOWER.NS', 'ADANIGREEN.NS',
          'AEGISLOG.NS', 'IGL.NS', 'MGL.NS', 'HINDPETRO.NS', 'CASTROLIND.NS',
          'GAIL.NS', 'GUJGASLTD.NS', 'PETRONET.NS', 'GSPL.NS', 'ATGL.NS',
          'OIL.NS', 'CHENNPETRO.NS', 'GMDCLTD.NS', 'MRPL.NS', 'SUZLON.NS',
          'INOXWIND.NS'
]

# stocks_list = ['XOM', 'CVX', '601857.SS', '600938.SS', 'WDS.AX',
#           'STO.AX', 'SHEL.L', 'BP-A.L', '1605.T', '5020.T'
# ]



# Dictionary mapping companies to industries
industry_dict = {
    'IOC': 'Refineries & Marketing',
    'POWERGRID': 'Power - Transmission',
    'RELIANCE': 'Refineries & Marketing',
    'NTPC': 'Power Generation',
    'COALINDIA': 'Coal',
    'ONGC': 'Oil Exploration & Production',
    'BPCL': 'Refineries & Marketing',
    'ADANIPOWER': 'Integrated Power Utilities',
    'TATAPOWER': 'Integrated Power Utilities',
    'ADANIGREEN': 'Power Generation',
    'AEGISLOG': 'Trading - Gas',
    'IGL': 'LPG/CNG/PNG/LNG Supplier',
    'MGL': 'LPG/CNG/PNG/LNG Supplier',
    'HINDPETRO': 'Refineries & Marketing',
    'CASTROLIND': 'Lubricants',
    'GAIL': 'Gas Transmission/Marketing',
    'GUJGASLTD': 'LPG/CNG/PNG/LNG Supplier',
    'PETRONET': 'LPG/CNG/PNG/LNG Supplier',
    'GSPL': 'Gas Transmission/Marketing',
    'ATGL': 'LPG/CNG/PNG/LNG Supplier',
    'OIL': 'Oil Exploration & Production',
    'CHENNPETRO': 'Refineries & Marketing',
    'GMDCLTD': 'Industrial Minerals',
    'MRPL': 'Refineries & Marketing',
    'SUZLON': 'Heavy Electrical Equipment',
    'INOXWIND': 'Heavy Electrical Equipment'

}

def download_stock_data(stocks_list, start_date, end_date):

  # Specify the directory to save the data
  save_directory = 'H:\My Drive\IIMA_Internship\Energy_Sector\Data\Processed'
  # Create the directory if it doesn't exist
  os.makedirs(save_directory, exist_ok=True)

# Fetching data for each stock
  for stock in stocks_list:
      # Download data from Yahoo Finance
      data = yf.download(stock, start=start_date, end=end_date, auto_adjust=False, multi_level_index=False)

      # Extract company name from the stock symbol (remove ".NS")
      company_name = stock.split('.')[0]

      # Perform transformations
      data['Previous day close price'] = data['Adj Close'].shift(1).squeeze()
      data['Change in price'] = data['Adj Close'] - data['Previous day close price']
      data['Percent change in price'] = data['Adj Close'].pct_change()
      data['Previous day volume'] = data['Volume'].shift(1).squeeze()
      data['Change in volume'] = data['Volume'] - data['Previous day volume']
      data['Percent change in volume'] = data['Volume'].pct_change()

      # Obtaining Moving averages (5-day, 20-day, 50-day, 100-day)

      # data['5_day_MA'] = data['Adj Close'].rolling(window = 5).mean()
      # data['20_day_MA'] = data['Adj Close'].rolling(window = 20).mean()
      # data['50_day_MA'] = data['Adj Close'].rolling(window = 50).mean()
      # data['100_day_MA'] = data['Adj Close'].rolling(window = 100).mean()

      # Add the industry information to the data
      data['Industry'] = industry_dict.get(company_name, 'Unknown')



      # Save the updated data to a CSV file in the specified directory
      file_path = os.path.join(save_directory, f'{company_name}.csv')
      data.to_csv(file_path, index=True)

      # Optionally, display a message after saving
      print(f'Successfully saved updated data for {company_name} at {file_path}')


  print("All files have been updated and saved successfully!")

download_stock_data(stocks_list, '2000-01-01', datetime.today().strftime('%Y-%m-%d'))


