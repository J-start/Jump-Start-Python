from coins import *
from selic import *
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def scheduleCoin():
    scheduler.enter(180, 1, scheduleCoin)
    getAllCoinsAndPrint()

def executeScheduleCoin():
    scheduleCoin()
    scheduler.run()

def scheduleSelic():
    scheduler.enter(180, 1, scheduleSelic)
    getSelic()

def executeScheduleSelic():
    scheduleSelic()
    print("a")
    scheduler.run()