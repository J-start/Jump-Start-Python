import requests
import json

def teste():
    request = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json")
    resp = request.json()
    return resp[0]
