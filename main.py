from api.scheduleConsumeApi import *
import threading
from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
from manipulation.acoes import *
from api.consumeGoogleSheets import *
import requests
import json

thread_coin = threading.Thread(target=getAllCoinsAndPrint)
thread_selic = threading.Thread(target=getSelic)
thread_crypto = threading.Thread(target=getAndPrintAllCryptos)
thread_action = threading.Thread(target=fetchAllInformationActions)
thread_coin.start()
thread_selic.start()
thread_crypto.start()
thread_action.start()

thread_coin.join()
thread_selic.join()
thread_crypto.join()
thread_action.join()




