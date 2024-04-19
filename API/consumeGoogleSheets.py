import requests
from dotenv import load_dotenv
load_dotenv()
import os

def insertDatasCoins(datas):
    url = os.environ["url"]
    response = requests.post(url, data=datas)
    if response.status_code == 200:
        print("Requisição POST bem-sucedida!")
    else:
        print("Erro na requisição:", response.status_code)