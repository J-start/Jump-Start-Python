from api.scheduleConsumeApi import *
import threading
from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
from manipulation.acoes import *
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *
import time

inicio = time.time()

#thread_coin = threading.Thread(target=getAllCoinsAndPrint)
#thread_selic = threading.Thread(target=manipulationSelic)
#thread_crypto = threading.Thread(target=getAndPrintAllCryptos)
#thread_action = threading.Thread(target=fetchAllInformationActions)
#
#thread_coin.start()
#thread_selic.start()
#thread_crypto.start()
#thread_action.start()
#
#thread_coin.join()
#thread_selic.join()
#thread_crypto.join()
#thread_action.join()
getAllCoinsAndPrint()
manipulationSelic()
getAndPrintAllCryptos()
fetchAllInformationActions()

fim = time.time()
timeFunction = fim - inicio
print("time: ",timeFunction)

# With threads => 33s
# WithOut threads => 46s



