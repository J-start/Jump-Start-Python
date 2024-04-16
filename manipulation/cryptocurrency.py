
import requests
import json

def cripto():

    data = {
    "OMSId": 1,
    "InstrumentId": 1,
    "Depth": 1
    }

# Cabeçalho da solicitação
    headers = {'Content-type': 'application/json'}

# Fazendo a solicitação POST
    response = requests.post("https://api.coinext.com.br:8443/AP/GetL2Snapshot", json=data, headers=headers)

    resp = response.json()
    print(resp)