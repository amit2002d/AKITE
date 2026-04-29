import yfinance as yf
import pandas as pd
from datetime import date

def download_niftybees_data():
    # Define the ticker symbol for NiftyBeES on NSE
    ticker = "NIFTYBEES.NS"
    
    # Define the date range: 1 Jan 2009 till present
    start_date = "2009-01-01"
    end_date = date.today().strftime('%Y-%m-%d')
    
    print(f"Downloading data for {ticker} from {start_date} to {end_date}...")
    
    # Fetch the data
    # auto_adjust=True ensures Open/High/Low/Close are adjusted for splits/dividends
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
    
    if not data.empty:
        # Save to CSV
        filename = f"{ticker.replace('.', '_')}_historical.csv"
        data.to_csv(filename)
        print(f"Successfully downloaded {len(data)} rows.")
        print(f"Data saved to {filename}")
        print(data.tail())
    else:
        print("No data found or failed to download.")

if __name__ == "__main__":
    download_niftybees_data()
