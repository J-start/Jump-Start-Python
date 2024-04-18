from api.consumeApi import *

def getSelic():
    request = getApiSelic()
    resp = request.json()
    print("-------- selic ------")
    print("date",resp[0]['data'])
    print("valor",resp[0]['valor'])
    return resp[0]
