from scheduleConsumeApi import *
import threading


thread_coin = threading.Thread(target=executeScheduleCoin)
thread_selic = threading.Thread(target=executeScheduleSelic)

thread_coin.start()
thread_selic.start()

thread_coin.join()
thread_selic.join()

print("Ambas as threads concluídas.")