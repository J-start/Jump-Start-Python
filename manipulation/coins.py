from api.consumeApi import getApiCoins

def getCoin(coin):
    request = getApiCoins(coin)
    if request.status_code == 200:
        resp = request.json()
        
        if coin != "USDT":
            return resp[f"{coin}BRL"]
        else:
            return resp["USDBRLT"]
    else:
        return "erro"
    
def getAllCoinsAndPrint():
    coins = ["AED","ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    for coin in coins:
        print("---------- Moedas ------------")
        high=round(float(getCoin(coin)['high']),5) 
        low=round(float(getCoin(coin)['low']),5)
        bid=round(float(getCoin(coin)['bid']),5)
        ask=round(float(getCoin(coin)['ask']),5)
        print("Code: ",getCoin(coin)['code'],"\t Name: ",getCoin(coin)['name'],"\t High: ",high,"\t Low: ","\t Low: ",low,"\t bid: ",bid,"\t ask: ",ask,'\n')
        print("---------- Moedas ------------")

def main():
    getAllCoinsAndPrint()
if __name__ == "__main__":
    main()