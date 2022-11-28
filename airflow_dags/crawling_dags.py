from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import urllib
from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import datetime
import pymysql
import os
import re
from sqlalchemy import create_engine
import time
from pprint import pprint
from datetime import datetime
from crawl.donga_news import donga
from crawl.chosun_news import chosun_crawl
from crawl.joongang_news import joongang_crawl
from crawl.khan_news import khan

args = {'owner':'youngdong'}


dag = DAG(dag_id = 'news_crawling_batch',
          default_args=args,
          start_date= datetime(22, 11, 10),
          catchup= False,
          description= 'pipe line batch process',
          schedule_interval = '* * * * *'
          )

t_now = datetime.now()

def donga_daily():
	for i in range():

		donga(t_now.strftime("%Y%m%d"))

def chosun_daily():
	chosun_crawl(int(t_now.strftime("%Y")),int(t_now.strftime("%m")),int(t_now.strftime("%d")))

def joongang_daily():
	joongang_crawl(t_now.strftime("%Y"),t_now.strftime("%m"),t_now.strftime("%d"))

def khan_daily():
	khan(t_now.strftime("%Y"),t_now.strftime("%m"),t_now.strftime("%d"))



crawling_one = PythonOperator(
	task_id = 'donga_news',
	python_callable =  donga_daily,
	dag = dag
)

crawling_two = PythonOperator(
	task_id = 'chosun_news',
	python_callable =  chosun_daily,
	dag = dag
)

crawling_three = PythonOperator(
	task_id = 'joongang_news',
	python_callable = joongang_daily,
	dag = dag
)
crawling_four = PythonOperator(
	task_id = 'khan_news',
	python_callable = khan_daily,
	dag = dag
)

crawling_one >> crawling_two >> crawling_three >> crawling_four
