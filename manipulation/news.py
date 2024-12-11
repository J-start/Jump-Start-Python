
import random
from API.consumeGoogleSheets import *

import json
from common.dataBaseCredentials import NAME_DATABASE
from dataBase.newsDB import *
from dataBase.insertDatas import *
from datetime import datetime
from gnews import GNews

SHARE_COUNT = [0,0]
COIN_COUNT = [0,0]
CRYPTO_COUNT = [0,0]

numbersAlreadyDrawn = []

def countAsset(listAssetNames):
    global SHARE_COUNT, COIN_COUNT, CRYPTO_COUNT
    for valor in listAssetNames:
        if valor[1] == "SHARE":
            SHARE_COUNT[1] += 1
        elif valor[1] == "COIN":
            COIN_COUNT[1] += 1
        elif valor[1] == "CRYPTO":
            CRYPTO_COUNT[1] += 1
    
    SHARE_COUNT[0] = getFirstOccurrence(listAssetNames,"SHARE")
    COIN_COUNT[0] = getFirstOccurrence(listAssetNames,"COIN")
    CRYPTO_COUNT[0] = getFirstOccurrence(listAssetNames,"CRYPTO")



def getFirstOccurrence(listAssetNames, assetP):
    for i, (asset, type) in enumerate(listAssetNames):
        if type == assetP:
            return i  
    return 0  
    

def drawAsset(typeAsset):
   
    if typeAsset == "SHARE":
        return draw(SHARE_COUNT[0],SHARE_COUNT[0] + SHARE_COUNT[1])
    elif typeAsset == "COIN":
        return draw(COIN_COUNT[0],COIN_COUNT[0] + COIN_COUNT[1])
    elif typeAsset == "CRYPTO":
       return draw(CRYPTO_COUNT[0],CRYPTO_COUNT[0] + CRYPTO_COUNT[1])

def draw(MIN,MAX):
    global numbersAlreadyDrawn
    number = random.randint(MIN,MAX)
    while number in numbersAlreadyDrawn:
        number = random.randint(MIN,MAX)
    numbersAlreadyDrawn.append(number)
    return number

def fetchListAsset():
    listAssetNames = getNameAsset(NAME_DATABASE)
    listAssetNames.sort(key=lambda x: x[1])

    return listAssetNames

def getAsset(listAsset, typeAsset):
    indexAsset = drawAsset(typeAsset)
    for i, (asset, type) in enumerate(listAsset):
        if i == indexAsset:
            return asset
    return asset


def searchAsset(typeAsset,listAsset):
    for i in range(3):
        asset = getAsset(listAsset,typeAsset)
        if typeAsset == "SHARE":
            messageShare = fetchNews("Ação "+asset)
            try:
                data = json.dumps(convertNewsToObject(messageShare,"SHARE"), ensure_ascii=False)
                insertNews(NAME_DATABASE,data,convertDateApiToDateMysql(messageShare['published date']))
            except Exception as e:
                datas = {
                    "Data": datetime.now(),
                    "Ativo": "Erro ao buscar noticia, google news ",
                    "Status": e
                }
                insertErrorGoogleSheets(datas)
                return
        elif typeAsset == "COIN":
            messageCoin = fetchNews("Moeda "+asset)
            try:
                data = json.dumps(convertNewsToObject(messageCoin,"COIN"), ensure_ascii=False)
                insertNews(NAME_DATABASE,data,convertDateApiToDateMysql(messageCoin['published date']))
            except Exception as e:
                datas = {
                    "Data": datetime.now(),
                    "Ativo": "Erro ao buscar noticia, google news ",
                    "Status": e
                }
                insertErrorGoogleSheets(datas)
                return
        elif typeAsset == "CRYPTO":
            messageCrypto = fetchNews("Cripto "+asset)
            try:
                data = json.dumps(convertNewsToObject(messageCrypto,"CRYPTO"), ensure_ascii=False)
                insertNews(NAME_DATABASE,data,convertDateApiToDateMysql(messageCrypto['published date']))
            except Exception as e:
                datas = {
                    "Data": datetime.now(),
                    "Ativo": "Erro ao buscar noticia, google news ",
                    "Status": e
                }
                insertErrorGoogleSheets(datas)
                return

def searchNews():
    listAsset = fetchListAsset()
    countAsset(listAsset)
    searchAsset("SHARE",listAsset)
    searchAsset("COIN",listAsset)
    searchAsset("CRYPTO",listAsset)       



def fetchNews(asset):
    google_news = GNews(language='pt', country='BR',max_results=2,period='7d')
    try:
        news = google_news.get_news(asset)
    except Exception as e:
        print("Erro ao buscar noticia, google news ",e)
        datas = {
            "Data": datetime.now(),
            "Ativo": "Erro ao buscar noticia, google news ",
            "Status": e
        }
        insertErrorGoogleSheets(datas)
        return
    
    for article in news:
        return article

def convertDateApiToDateMysql(date):
    date_obj = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S GMT')
    mysql_date_str = date_obj.strftime('%Y-%m-%d')
    return mysql_date_str

def convertNewsToObject(messageShare,typeAsset):
        data = {
         typeAsset: {
            "description": messageShare['description'],
                "url": messageShare['url']
                }
            }
        return data
    
         
