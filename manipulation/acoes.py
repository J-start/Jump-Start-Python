import yfinance as yf 
from datetime import datetime, timedelta
from API.consumeGoogleSheets import *
from datetime import datetime
from dataBase.insertDatas import *
from dataBase.updateDatas import *
from common.listShares import *

dateActual = datetime.now()
dateBeforeActual = dateActual - timedelta(days=1)

def fetchInformationAction(dataBase,share):
    try:
        data = yf.download(share, start=dateBeforeActual, progress=False)

        if len(data.values) != 0:
            latest_data = data.iloc[-1] 
            open = round(latest_data.values[0],4)
            high = round(latest_data.values[1],4)
            low = round(latest_data.values[2],4)
            close = round(latest_data.values[3],4)
            volume = round(latest_data.values[5],4)
            if volume == 0:
                return
            date = getDateActual()
            insertDatasActions(dataBase,share,date,open,high,low,close,volume)
    except Exception as e:
            print("erro: ", e)
            manipluationError(e,"Erro ao manipular ações")

    
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

