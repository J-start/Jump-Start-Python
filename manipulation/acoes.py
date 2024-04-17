import yfinance as yf 
data_vale = yf.download("MGLU3.SA", start="2024-04-17", progress=False)
print(data_vale)
#data_value.values[i]