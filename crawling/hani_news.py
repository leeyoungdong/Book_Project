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
import datetime
from urllib.request import HTTPError

hani_url= 'https://www.hani.co.kr/arti/culture/culture_general/{}.html'
# 1068411

def hani_news(date):


    hani_data = pd.DataFrame()

    url = hani_url.format(date)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    try:
      category = soup.select_one("p.category > span").get_text()
      result = soup.select_one("h4 > span").get_text()
      pdate = soup.select_one('p.date-time > span:nth-child(1)').get_text()
      hani_data = pd.DataFrame({'category':category,'title':result,'pdate':pdate}, index=[0])
    
    except AttributeError as e:
      print(e,'영어 뉴스 패스')
      pass
    
    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    hani_data.to_sql('hani_news',if_exists = 'append', con = engine)
    con.commit()

if __name__ == '__main__':
  for i in range(639636,1068411):
    try:
      print(i) 
      hani_news(i)

    except HTTPError as e:
      print(e)
      pass