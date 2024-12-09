from gnews import GNews

def searchNews():


    google_news = GNews(language='pt', country='BR',max_results=10,period='7d')
    news = google_news.get_news('Ações banco do brasil')

    for article in news:
        print("published date \n",article['published date'])
        print("descricao \n",article['description'])
        #print(article['title'],article['description'], article['url'])

def main():
    searchNews()

if __name__ == "__main__":
    main()

