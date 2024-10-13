

from GoogleNews import GoogleNews
import random
import datetime

def fetchNews(messageToSearch,index):

    googlenews = GoogleNews()
    googlenews.enableException(True)
    googlenews.set_lang('pt-br')
    googlenews.set_period('1d')
    googlenews.set_encode('utf-8')
    try:
        googlenews.search(messageToSearch)
    except:
        print("erro")
    googlenews.get_page(1)
    print(messageToSearch)
    news = googlenews.get_texts()
    return news[index]


def makeRequests(context):
    convertDays = {0: 0, 1: 3, 2: 6,3: 9, 4: 12, 5: 15, 6: 18}
    numberDayWeek = datetime.datetime.now().weekday()

    startNews = convertDays[numberDayWeek]
    limitNews = startNews + 2

    if numberDayWeek == 6:
        startNews -= 1
        limitNews -= 1

    listNews = []

    for i in range(startNews, limitNews + 1):
       listNews.append(fetchNews(context,i))

    return listNews



def main():
    actions = ["PETR4.SA", "BBAS3.SA", "ITSA4.SA", "TRPL4.SA", "VALE3.SA", "CMIG4.SA", "SANB11.SA", "USIM5.SA",
               "ABEV3.SA", "MGLU3.SA"]

    coins = ["Peso Argentino", "Dólar Australiano", "Moeda Boliviano", "Dólar Canadense", "Franco Suíço ", "Peso Chileno", "Yuan Chinês", "Peso Colombiano", "Coroa Dinamarquesa", "Euro", "Dólar de Hong Kong", "Rúpia Indiana", "Iene Japonês", "Peso Mexicano", "Coroa Norueguesa",
             "Guarani Paraguaio ", "Rublo Russo", "Coroa Sueca", "Dólar Taiuanês", "Dólar Americano ", "Peso Uruguaio", "Bolívar Venezuelano"]

    cryptos = ["BTC", "LTC", "ETH", "XRP", "BCH", "USDT", "LINK", "DOGE", "ADA", "EOS", "XLM", "CHZ", "AXS"]
    listNewsFinal = []
    CRYPTO = random.randint(0, 12)
    COINS = random.randint(0, 21)
    ACTIONS = random.randint(0, 9)

    try:
        listNewsFinal += listNewsFinal + makeRequests(actions[ACTIONS])
        listNewsFinal += listNewsFinal + makeRequests(coins[COINS])
        listNewsFinal += listNewsFinal + makeRequests(cryptos[CRYPTO])
        listNewsFinal += listNewsFinal + makeRequests("Selic")
    except Exception as e:
        print("Erro :", e)
    print(listNewsFinal)

if __name__ == "__main__":
    main()



#datas[i]