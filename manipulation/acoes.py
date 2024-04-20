import yfinance as yf 
from datetime import datetime, timedelta
from api.consumeGoogleSheets import *
from datetime import datetime

dateActual = datetime.now()
dateBeforeActual = dateActual - timedelta(days=1)

dateFormated = dateBeforeActual.strftime('%Y-%m-%d')

def fetchInformationAction(action):

    data = yf.download(action, start=dateFormated, progress=False)
    if len(data.values) != 0:
        if len(data.values) == 2:
            print("name-action",action,"Open: ",data.values[1][0].round(2),"High: ",data.values[1][1].round(2),"\t ","LOW: ",data.values[1][2].round(2),"\t ","Close: ",data.values[1][3].round(2),"\t ","\t ","Volume: ",data.values[1][5].round(0))
        elif len(data.values) == 1:
            print("name-action",action,"Open: ",data.values[0][0].round(2),"High: ",data.values[0][1].round(2),"\t ","LOW: ",data.values[0][2].round(2),"\t ","Close: ",data.values[0][3].round(2),"\t ","\t ","Volume: ",data.values[0][5].round(0))
    else:
            dados = {
                "Data": "",
                "Ativo": f"Ação: {action}",
                "Status": "400"
                }
            insertDatasCoins(dados)
    
def fetchAllInformationActions():
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    for action in actions:
        print("----------- ACOES ----------")
        fetchInformationAction(action)


# se len(data_vale.values) ==2 sinal que possui dados das ações do dia atual, se len() ==1 informações do dia anterior

# data.values[0][0] => open
# data.values[0][1] => high
# data.values[0][2] => low
# data.values[0][3] => close
# data.values[0][5] => volume
