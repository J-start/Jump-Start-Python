import requests
import json

def get_something():
    request = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    print("status code response: ", request.status_code)
    #print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)
    resp = request.json()
    print("resp[USDBRL][ask]",resp['USDBRL']['ask'])