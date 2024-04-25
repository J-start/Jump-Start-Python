from api.scheduleConsumeApi import *
from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
from manipulation.acoes import *
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *

import time
import threading


inicio = time.time()

thread_coin = threading.Thread(target=getAllCoinsAndPrint("jumpstart"))
thread_selic = threading.Thread(target=manipulationSelic("jumpstart"))
thread_crypto = threading.Thread(target=getAndPrintAllCryptos("jumpstart"))
thread_action = threading.Thread(target=fetchAllInformationActions("jumpstart"))

thread_coin.start()
thread_selic.start()
thread_crypto.start()
thread_action.start()

thread_coin.join()
thread_selic.join()
thread_crypto.join()
thread_action.join()

#getAllCoinsAndPrint()
#manipulationSelic()
#getAndPrintAllCryptos()
#fetchAllInformationActions()

fim = time.time()
timeFunction = fim - inicio
print("time: ",timeFunction)

# With threads => 33s
# WithOut threads => 46s



