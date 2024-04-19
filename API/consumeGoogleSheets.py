import requests

def insertDatasCoins(datas):
    url = 'https://script.google.com/macros/s/AKfycbycSeOU7amm20Xns6RxscpSa8FElMMRpXigbuFwugcVKhPZpiTFD2OLCVLjswnniuFJ/exec'
    response = requests.post(url, data=datas)
    if response.status_code == 200:
        print("Requisição POST bem-sucedida!")
    else:
        print("Erro na requisição:", response.status_code)