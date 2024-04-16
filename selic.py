from consumeApi import *

def getSelic():
    request = getApiSelic()
    resp = request.json()
    print("res",resp)
    return resp[0]
