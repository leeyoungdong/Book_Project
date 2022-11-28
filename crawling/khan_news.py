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

khan_URL = 'https://www.khan.co.kr/sitemap.html?year={}&month={}&day={}'

def khan(year, month, day):
    
    khan_data = pd.DataFrame()

    headers={'User-Agent': 'Mozilla/5.0'}
    url = khan_URL.format(year, month, day)
    request = Request(url, headers=headers)
    html = urlopen(request).read()
    soup = bs(html, 'html.parser')
    result = soup.select('ul.daynews_list > li')

    for posts in result:
        context = posts.select_one('[title]').text
        # print(context)
        df = pd.DataFrame({'context':context}, index = [0])
        khan_data = khan_data.append(df, ignore_index = True)

    news_date = year+month+day
    khan_data['date'] = news_date
    
    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    khan_data.to_sql('khan_news',if_exists = 'append', con = engine)
    con.commit()

# a = datetime.datetime(2000, 1, 1) + datetime.timedelta(days= 1 - 1)
# print(a.strftime("%Y"),a.strftime("%m"),a.strftime("%d"))

if __name__ == '__main__':

    for i in range(1, 8200):
        print(i)
        a = datetime.datetime(2000, 7, 27) + datetime.timedelta(days= i - 1)
        khan(a.strftime("%Y"),a.strftime("%m"),a.strftime("%d"))
