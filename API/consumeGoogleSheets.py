import requests

def insertDatasCoins(datas):
    url = 'https://script.google.com/macros/s/AKfycbycSeOU7amm20Xns6RxscpSa8FElMMRpXigbuFwugcVKhPZpiTFD2OLCVLjswnniuFJ/exec'
    response = requests.post(url, data=datas)
    if response.status_code == 200:
        print("Requisição POST bem-sucedida!")
    else:
        print("Erro na requisição:", response.status_code)

def insertDatasCrypto(datas):
    url = 'https://script.google.com/macros/s/AKfycbyKNakGtxRlCR1VZkBHTsrx0W8T6zj4nz6_s8bvmWsulqvpjy0XFWMURPiL9w5jbb0QnQ/exec'
    response = requests.post(url, data=datas)
    if response.status_code == 200:
        print("Requisição POST bem-sucedida!")
    else:
        print("Erro na requisição:", response.status_code)