from api.consumeApi import *
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *
from datetime import datetime

def getSelic():
    request = getApiSelic()
    if request.status_code == 200:
        resp = request.json()
        value = round(float(resp[0]['valor']),4)
        dateActual = generatedDateActual()
        try:
            insertDatasSelic(dateActual,value)
        except:
            print("erro")
            #TODO - insert log    
    else:
        dados = {
                "Data": "",
                "Ativo": "Selic",
                "Status": request.status_code
                }
        insertDatasCoins(dados)
        return "erro"
    
def generatedDateActual():
   dataActual = datetime.now() 
   dateFormated = dataActual.strftime('%Y-%m-%d')
   return dateFormated


# print("-------- selic ------")
# print("date",resp[0]['data'])
# print("valor",resp[0]['valor'])