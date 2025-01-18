from waitress import serve
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from manipulation.crypto import mainCrypto
from manipulation.news import searchNews
from manipulation.acoes import fetchAllInformationActions
from common.dataBaseCredentials import NAME_DATABASE
import time

app = Flask(__name__)
brazil_tz = pytz.timezone('America/Sao_Paulo')

def fetch_actions_task():
    print("Executando tarefa de buscar ações...")
    fetchAllInformationActions(NAME_DATABASE)

def fetch_crypto_task():
    print("Executando tarefa de buscar crypto...")
    mainCrypto(NAME_DATABASE)

def search_news_task():
    print("Executando tarefa de buscar notícias...")
    searchNews()

scheduler = BackgroundScheduler(timezone=brazil_tz)

scheduler.add_job(search_news_task, CronTrigger(hour=11, minute=10), name="Search News at 11:10")

scheduler.add_job(fetch_crypto_task, CronTrigger(hour=11, minute=15), name="Fetch crypto at 11:15")

scheduler.add_job(fetch_actions_task, CronTrigger(hour=10, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 10:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=10, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 10:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=11, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 11:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=11, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 11:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=12, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 12:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=12, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 12:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=13, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 13:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=13, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 13:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=14, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 14:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=14, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 14:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=15, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 15:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=15, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 15:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=16, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 16:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=16, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 16:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=17, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 17:00")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=17, minute=30, day_of_week="mon-fri"), name="Fetch Actions at 17:30")
scheduler.add_job(fetch_actions_task, CronTrigger(hour=18, minute=0, day_of_week="mon-fri"), name="Fetch Actions at 18:00")

scheduler.start()

print("Agendador iniciado. Todas as horas no horário de Brasília.")
searchNews()

