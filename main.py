from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from manipulation.news import *
from manipulation.acoes import *
from common.dataBaseCredentials import NAME_DATABASE


brazil_tz = pytz.timezone('America/Sao_Paulo')


def fetch_actions_task():
    fetchAllInformationActions(NAME_DATABASE)

def search_news_task():
    searchNews()

scheduler = BlockingScheduler()

scheduler.add_job(search_news_task, 
                  trigger=CronTrigger(hour=11, minute=10, timezone=brazil_tz),
                  name="Search News at 11:10")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=10, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 10:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=10, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 10:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=11, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 11:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=11, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 11:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=12, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 12:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=12, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 12:30")


scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=13, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 13:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=13, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 13:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=14, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 14:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=14, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 14:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=15, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 15:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=15, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 15:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=16, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 16:00")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=16, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 16:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=17, minute=30, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 17:30")

scheduler.add_job(fetch_actions_task, 
                  trigger=CronTrigger(hour=18, minute=0, day_of_week="mon-fri", timezone=brazil_tz),
                  name="Fetch Actions at 18:00")


print("Agendador iniciado. Todas as horas no horário de Brasília.")
scheduler.start()
