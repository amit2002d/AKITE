import yfinance as yf

def get_cmp_price(cmp_symbol):
    try:
        cmp_data = yf.Ticker(cmp_symbol)
        print(cmp_data)
        cmp_price = cmp_data.history(period="1mo")["Close"]
        return cmp_price
    except Exception as e:
        return None

print(get_cmp_price("MSFT"))