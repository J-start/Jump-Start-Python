

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

    listNews = []

    for i in range(startNews, limitNews + 1):
       listNews.append(fetchNews(context,i))

    return listNews



def main():
    listNewsFinal = []
    listNewsFinal += listNewsFinal + makeRequests("Bitcoin")
    listNewsFinal += listNewsFinal + makeRequests("Selic")
    listNewsFinal += listNewsFinal + makeRequests("Ação banco do brasil")
    listNewsFinal += listNewsFinal + makeRequests("Dolar")
    print(listNewsFinal)


if __name__ == "__main__":
    main()



#datas[i]