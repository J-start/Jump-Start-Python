import requests

def searchListShares():
    url = "http://localhost:8080/asset/request/?type=SHARE"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Erro na requisição google sheets:", str(e))
        return None
    if response.status_code != 200:
        print("Erro na requisição google sheets:", response.status_code)
    else:
        return response.text.replace('"',"").split(",")


def main():
    searchListShares()

if __name__ == "__main__":
    main()    

