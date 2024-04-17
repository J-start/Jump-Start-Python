from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def scheduleCoin():
    scheduler.enter(900, 1, scheduleCoin)
    getAllCoinsAndPrint()

def executeScheduleCoin():
    scheduleCoin()
    scheduler.run()

def scheduleSelic():
    scheduler.enter(900, 1, scheduleSelic)
    getSelic()

def executeScheduleSelic():
    scheduleSelic()
    scheduler.run()

def scheduleCrypto():
    scheduler.enter(900, 1, getAndPrintAllCryptos)
    getAndPrintAllCryptos()

def executeScheduleCrypto():
    scheduleCrypto()
    scheduler.run()