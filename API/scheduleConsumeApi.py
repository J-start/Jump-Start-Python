from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
from manipulation.acoes import *
import sched
import time
import threading

scheduler = sched.scheduler(time.time, time.sleep)

TIMESCHEDULE = 1800


def execute():
    begin = time.time()

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
    
    end = time.time()
    timeFunction = end - begin

    print("time: ",timeFunction)

def schedule():
    scheduler.enter(TIMESCHEDULE, 1, schedule)
    execute()

def executeSchedule():
    schedule()
    scheduler.run()




