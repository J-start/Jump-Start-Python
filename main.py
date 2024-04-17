from API.scheduleConsumeApi import *
import threading



thread_coin = threading.Thread(target=executeScheduleCoin)
thread_selic = threading.Thread(target=executeScheduleSelic)
thread_crypto = threading.Thread(target=executeScheduleCrypto)

thread_coin.start()
thread_selic.start()
thread_crypto.start()

thread_coin.join()
thread_selic.join()
thread_crypto.join()