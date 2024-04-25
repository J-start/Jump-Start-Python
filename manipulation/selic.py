from api.consumeApi import *
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *
from datetime import datetime
from dataBase.updateDatas import *

def manipulationSelic(dataBase):
    request = getApiSelic()
    if request.status_code == 200:
        resp = request.json()
        
        value = round(float(resp[0]['valor']),4)
        dateActual = convertDateApiToDateDataBase(resp[0]['data'])
        
        try:
            insertDatasSelic(dataBase,dateActual,value)
            try:
                manipulationSelicDeleteDatas(dataBase)
            except:
                print("erro manipulationSelic")
        except:
            print("erro")
            #TODO - insert log    
    else:
        dados = {
                "Data": "",
                "Ativo": "Selic",
                "Status": request.status_code
                }
        insertErrorGoogleSheets(dados)
        return "erro"
    
def convertDateApiToDateDataBase(dateApi):
    dateApiToConvert = datetime.strptime(dateApi, '%d/%m/%Y')
    dateFormated = dateApiToConvert.strftime('%Y-%m-%d')

    return dateFormated


# print("-------- selic ------")
# print("date",resp[0]['data'])
# print("valor",resp[0]['valor'])