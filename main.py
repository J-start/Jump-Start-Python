from API.scheduleConsumeApi import *
from manipulation.coins import *
from manipulation.selic import *
from manipulation.cryptocurrency import *
from manipulation.news import *
import schedule

HOUR_DAY_1_ACTION = "17:57"
HOUR_DAY_2_ACTION = "17:58"
HOUR_DAY_3_ACTION = "17:59"
HOUR_DAY_4_ACTION = "18:00"

HOUR_DAY_NEWS = "13:00"

HOUR_DAY_SELIC = "17:57"

schedule.every().day.at(HOUR_DAY_NEWS).do(insertInDataBase) # NEWS


schedule.every(10).minutes.do(getAndPrintAllCryptos, "jumpStart") # CRYPTOS

schedule.every().day.at(HOUR_DAY_SELIC).do(manipulationSelic, "jumpStart") # SELIC

schedule.every().day.at(HOUR_DAY_1_ACTION).do(fetchAllInformationActions, "jumpStart") # ACAO
schedule.every().day.at(HOUR_DAY_2_ACTION).do(fetchAllInformationActions, "jumpStart")
schedule.every().day.at(HOUR_DAY_3_ACTION).do(fetchAllInformationActions, "jumpStart")
schedule.every().day.at(HOUR_DAY_4_ACTION).do(fetchAllInformationActions, "jumpStart") # ACAO

schedule.every().hour.do(getAllCoinsAndPrint, "jumpStart") # COINS


while True:
    schedule.run_pending()
    time.sleep(1)




