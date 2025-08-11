import yfinance as yf
import os

# Define the tickers and the date range
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = '2025-07-31'

# Define the directory to save the data
data_dir = 'data'

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Fetch and save the data for each ticker
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(os.path.join(data_dir, f'{ticker}.csv'))
    print(f'Successfully downloaded and saved data for {ticker}')
