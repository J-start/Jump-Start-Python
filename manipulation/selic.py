from api.consumeApi import *
from api.consumeGoogleSheets import *
from datetime import datetime


def getSelic():
    request = getApiSelic()
    if request.status_code == 200:
        resp = request.json()
        print("-------- selic ------")
        print("date",resp[0]['data'])
        print("valor",resp[0]['valor'])
        return resp[0]
    else:
        dateActual = datetime.now()
        dados = {
                "Data": dateActual,
                "Ativo": "Selic",
                "Status": request.status_code
                }
        insertDatasCoins(dados)
        return "erro"
