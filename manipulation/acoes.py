import yfinance as yf 
from datetime import datetime, timedelta
from API.consumeGoogleSheets import *
from datetime import datetime
from dataBase.insertDatas import *
from dataBase.updateDatas import *
from common.listShares import *

dateActual = datetime.now()
dateBeforeActual = dateActual - timedelta(days=1)

dateFormated = dateBeforeActual.strftime('%Y-%m-%d')

def fetchInformationAction(dataBase,share):

    data = yf.download(share, start=dateFormated, progress=False)

    if len(data.values) != 0:
        date = getDateActual()
        open = data.values[0][0].round(4)
        high = data.values[0][1].round(4)
        low = data.values[0][2].round(4)
        close = data.values[0][3].round(4)
        volume = data.values[0][5].round(0)
        #if volume == 0:
            #return
        try:
            insertDatasActions(dataBase,share,date,open,high,low,close,volume)
        except:
            manipluationError(share,"Erro ao inserir dados no banco de dados")

    
def fetchAllInformationActions(dataBase):
    actions = searchListShares()
    for action in actions:
        fetchInformationAction(dataBase,action)
    try:
        manipulationAcoes(dataBase)
    except Exception as e:
        manipluationError(action, f"Erro ao manipular acoes, verificação de exclusão: ${str(e)}")


def manipluationError(share,status):
     datas = {
            "Data": "",
            "Acao": share,
            "Status": status
             }
     insertErrorGoogleSheets(datas) 

def getDateActual():
    dateActualFormated = dateActual.strftime('%Y-%m-%d')
    return dateActualFormated

