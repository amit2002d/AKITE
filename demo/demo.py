import yfinance as yf

cmp_data = yf.Ticker("NIFTYBEES"+".NS")
cmp_price = cmp_data.history(period="1d")["Close"].iloc[-1]
cmp_history = cmp_data.history(period="1d")
print(cmp_history)