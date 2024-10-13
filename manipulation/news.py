

from GoogleNews import GoogleNews
import random
import datetime
from API.consumeGoogleSheets import *
from dataBase.insertDatas import *
import json

actions = ["PETR4.SA", "BBAS3.SA", "ITSA4.SA", "TRPL4.SA", "VALE3.SA", "CMIG4.SA", "SANB11.SA", "USIM5.SA","ABEV3.SA", "MGLU3.SA"]
coins   = ["Peso Argentino", "Dólar Australiano", "Moeda Boliviano", "Dólar Canadense", "Franco Suíço ", "Peso Chileno","Yuan Chinês", "Peso Colombiano", "Coroa Dinamarquesa", "Euro", "Dólar de Hong Kong", "Rúpia Indiana","Iene Japonês", "Peso Mexicano", "Coroa Norueguesa","Guarani Paraguaio ", "Rublo Russo", "Coroa Sueca", "Dólar Taiuanês", "Dólar Americano ", "Peso Uruguaio","Bolívar Venezuelano"]
cryptos = ["BTC", "LTC", "ETH", "XRP", "BCH", "USDT", "LINK", "DOGE", "ADA", "EOS", "XLM", "CHZ", "AXS"]

CRYPTO  = random.randint(0, 12)
COINS   = random.randint(0, 21)
ACTIONS = random.randint(0, 9)

DATABASE = "jumpStart"

def fetchNews(messageToSearch,index):

    googlenews = GoogleNews()
    googlenews.enableException(True)
    googlenews.set_lang('pt-br')
    googlenews.set_period('1d')
    googlenews.set_encode('utf-8')
    try:
        googlenews.search(messageToSearch)
    except:
        print("erro")
    googlenews.get_page(1)
    news = googlenews.get_texts()
    return news[index]


def makeRequests(context):
    convertDays = {0: 0, 1: 3, 2: 6,3: 9, 4: 12, 5: 15, 6: 18}
    numberDayWeek = datetime.datetime.now().weekday()

    startNews = convertDays[numberDayWeek]
    limitNews = startNews + 2

    if numberDayWeek == 6:
        startNews -= 1
        limitNews -= 1

    listNews = []

    for i in range(startNews, limitNews + 1):
       listNews.append(fetchNews(context,i))

    return listNews

def buildJsonBasedContext(listAsset,assetToSearch,assetKeyJson):
    json_data = []
    try:
        listToJson = makeRequests(listAsset[assetToSearch])
        json_data = [{assetKeyJson: asset} for asset in listToJson]
        return json_data
    except Exception as e:
        datas = {
            "Data": "",
            "Crypto": assetKeyJson + ' -> google news ' +  listAsset[assetToSearch],
            "Status": e
        }
        insertErrorGoogleSheets(datas)
        return json_data



def buildJsonSelic():
    json_data = []
    try:
        listSelic = makeRequests("Selic")
        json_data += [{"SELIC": selic} for selic in listSelic]
        return json_data
    except Exception as e:
        datas = {
            "Data": "",
            "Crypto":"selic-google news",
            "Status": e
        }
        insertErrorGoogleSheets(datas)

        return json_data

def insertInDataBase():
    json_data = []
    if buildJsonBasedContext(cryptos, CRYPTO, "CRYPTO"):
        json_data += buildJsonBasedContext(cryptos, CRYPTO, "CRYPTO")
    if buildJsonBasedContext(actions, ACTIONS, "Ação"):
        json_data += buildJsonBasedContext(actions, ACTIONS, "Ação")
    if buildJsonBasedContext(coins, COINS, "MOEDA"):
        json_data += buildJsonBasedContext(coins, COINS, "MOEDA")
    if buildJsonSelic():
        json_data += buildJsonSelic()
    json_string = json.dumps(json_data, ensure_ascii=False, indent=4)
    insertNews(DATABASE, json_string)


def main():
    print()

if __name__ == "__main__":
    main()



#datas[i] except Exception as e: makeRequests(actions[ACTIONS])