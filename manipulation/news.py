

from GoogleNews import GoogleNews
import random
from datetime import datetime
from API.consumeGoogleSheets import *
from dataBase.insertDatas import *
import json
from common.dataBaseCredentials import NAME_DATABASE

actions  = ["PETR4.SA", "BBAS3.SA", "ITSA4.SA", "TRPL4.SA", "VALE3.SA", "CMIG4.SA", "SANB11.SA", "USIM5.SA","ABEV3.SA", "MGLU3.SA"]
coins    = ["moeda Peso Argentino", "moeda Dólar Australiano", "Moeda Boliviano", "moeda Dólar Canadense", "moeda Franco Suíço ", "moeda Peso Chileno","Yuan Chinês", "moeda Peso Colombiano", "moeda Coroa Dinamarquesa", "moeda Euro", "moeda Dólar de Hong Kong", "moeda Rúpia Indiana","moeda Iene Japonês", "moeda Peso Mexicano", "moeda Coroa Norueguesa","moeda Guarani Paraguaio ", "moeda Rublo Russo", "moeda Coroa Sueca", "moeda Dólar Taiuanês", "moeda Dólar Americano ", "moeda Peso Uruguaio","moeda Bolívar Venezuelano"]
cryptos  = ["BTC", "LTC", "ETH", "XRP", "BCH", "USDT", "LINK", "DOGE", "ADA", "EOS", "XLM", "CHZ", "AXS"]

CRYPTO   = random.randint(0, len(cryptos) - 1)

ACTIONS  = random.randint(0, len(actions) - 1)

DATABASE = NAME_DATABASE

def fetchNews(messageToSearch,index):

    googlenews = GoogleNews()
    googlenews.enableException(True)
    googlenews.set_lang('pt-br')
    googlenews.set_period('1d')
    googlenews.set_encode('utf-8')
    try:
        googlenews.search(messageToSearch)
    except Exception as e:
        datas = {
            "Data": "",
            "Ativo": "Erro ao buscar noticia, google news ",
            "Status": e
        }
        insertErrorGoogleSheets(datas)
        return []
    googlenews.get_page(1)
    news = googlenews.get_texts()
    return news[index]


def insertNIntoDataBase():
    for i in range(0, 4):
        insertSelicDataBase(i)
        insertCryptoDataBase(i)
        insertCoinsDataBase(i)
        insertShareDataBase(i)

def insertShareDataBase(index):
    actionsIndex = random.randint(0, len(actions) - 1)
    messageShare = fetchNews(actions[actionsIndex], index)

    data = {
        "AÇÃO": messageShare

    }
    json_string = json.dumps(data, ensure_ascii=False)
    insertNews(DATABASE, json_string)

def insertCoinsDataBase(index):
    coinsIndex = random.randint(0, len(coins) - 1)
    messageShare = fetchNews(coins[coinsIndex], index)

    data = {
        "MOEDA": messageShare

    }
    json_string = json.dumps(data, ensure_ascii=False)
    insertNews(DATABASE, json_string)

def insertSelicDataBase(i):
    messageShare = fetchNews("selic", i)

    data = {
        "SELIC": messageShare

    }
    json_string = json.dumps(data, ensure_ascii=False)
    insertNews(DATABASE, json_string)

def insertCryptoDataBase(index):
    cryptoIndex = random.randint(0, len(cryptos) - 1)
    messageShare = fetchNews(cryptos[cryptoIndex], index)

    data = {
        "CRYPTO": messageShare

    }
    json_string = json.dumps(data, ensure_ascii=False)
    insertNews(DATABASE, json_string)

def main():
    insertNIntoDataBase()

if __name__ == "__main__":
    main()



