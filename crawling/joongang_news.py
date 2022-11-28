import time
import urllib
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from datetime import date
import datetime
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from urllib.request import HTTPError

joongang_URL = 'https://www.joongang.co.kr/sitemap/index/{}/{}/{}'

def joongang_crawl(year, month, day):


    joongang_data = pd.DataFrame()
    url = joongang_URL.format(year, month, day)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    result = soup.select("li.card")


    for post in result:
        context = post.select_one("h2.headline").text

        try:
            date = post.select_one("p.date")
        except AttributeError as e:
            print(e)
            pass
        df = pd.DataFrame({'context':context,'date':date}, index = [0])
        joongang_data = joongang_data.append(df, ignore_index = True)
    
    joongang_data = joongang_data[5:]

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    joongang_data.to_sql('joongang_news',if_exists = 'append', con = engine)
    con.commit()


if __name__ == '__main__':
    

    for i in range(1, 8360):
        print(i)
        a = datetime.datetime(2000, 1, 1) + datetime.timedelta(days= i - 1)
        joongang_crawl(a.strftime("%Y/%m/%d"))

