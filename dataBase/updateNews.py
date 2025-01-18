from dataBase.newsDB import deleteNewsById, getCountNews, getOldestNews
from dataBase.updateDatas import deleteAssets

def deleteOldestNews():
    idDelete = getOldestNews()
    if idDelete != -1:
        try:
            deleteNewsById(idDelete)
        except Exception as e:
            print("erro ao deletar noticia de id ",idDelete," erro: ", e)

def managerNews():
    MAX_NEWS = 50
    try:
        countNews = getCountNews()
    except Exception as e:
            print("erro ao buscar contagem de noticias ","erro: ", e)        
    if countNews != -1:
        if countNews > MAX_NEWS:
            deleteOldestNews()
