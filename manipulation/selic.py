from api.consumeApi import *
from api.consumeGoogleSheets import *

def getSelic():
    request = getApiSelic()
    if request.status_code == 200:
        resp = request.json()
        print("-------- selic ------")
        print("date",resp[0]['data'])
        print("valor",resp[0]['valor'])
        return resp[0]
    else:
        dados = {
                "Data": "",
                "Ativo": "Selic",
                "Status": request.status_code
                }
        insertDatasCoins(dados)
        return "erro"
