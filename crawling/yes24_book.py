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


yes24_week_url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=08&year={}&month={}&week={}&day=1&PageNumber={}' # 주간 week 5개있음음
yes24_day_url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=07&year={}&month={}&day={}&PageNumber={}' # 일간
yes24_year_url = 'http://www.yes24.com/24/category/bestseller?categorynumber=001&sumgb=09&year={}&month={}&pagenumber={}' # 월간

def yes24_day(year, month, day, page):
    
    yes24_day_data = pd.DataFrame()

    url = yes24_day_url.format(year, month, day, page)
    response = urllib.request.urlopen(url)
    soup = bs(response, 'html.parser')
    result = soup.select('td.goodsTxtInfo')
    day_date = str(year)+ str(month) + str(day)

    for i, post in enumerate(result):
      try:
        rank =  soup.select_one(f'#goods{i+1+20*(page-1)}').text
        review = post.select_one('p.review > a').text
        context = post.select_one('p:nth-of-type(1)').text
        auther = post.select_one('div').text
        df = pd.DataFrame({'rank':rank,'context':context,'review':review,'auther':auther}, index = [0])
        yes24_day_data = pd.concat([yes24_day_data,df])
      except AttributeError as e:
        print(e)
        print(i)
        pass

    yes24_day_data['date'] = day_date

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='!As36190301',
                            db='yoyoyo',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:!As36190301@localhost/yoyoyo')
    yes24_day_data.to_sql('yes24_day',if_exists = 'append', con = engine)
    con.commit()


yes24_week_url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=08&year={}&month={}&week={}&day=1&PageNumber={}' # 주간 week 5개있음음
yes24_day_url = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=07&year={}&month={}&day={}&PageNumber={}' # 일간
yes24_year_url = 'http://www.yes24.com/24/category/bestseller?categorynumber=001&sumgb=09&year={}&month={}&pagenumber={}' # 월간

def yes24_week(year, month, week, page):
    
    yes24_week_data = pd.DataFrame()

    url = yes24_week_url.format(year, month, week, page)
    response = urllib.request.urlopen(url)
    soup = bs(response, 'html.parser')
    result = soup.select('td.goodsTxtInfo')
    week_date = str(year)+ str(month) + str(week)

    for i, post in enumerate(result):
      try:
        rank =  soup.select_one(f'#goods{i+1+20*(page-1)}').text
        review = post.select_one('p.review > a').text
        context = post.select_one('p:nth-of-type(1)').text
        auther = post.select_one('div').text
        df = pd.DataFrame({'rank':rank,'context':context,'review':review,'auther':auther}, index = [0])
        yes24_week_data = pd.concat([yes24_week_data,df])
      except AttributeError as e:
        print(e)        
        print(i)
        pass
      
    yes24_week_data['date'] = week_date

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='!As36190301',
                            db='yoyoyo',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:!As36190301@localhost/yoyoyo')
    yes24_week_data.to_sql('yes24_week',if_exists = 'append', con = engine)
    con.commit()


def yes24_year(year, month, page):
    
    yes24_year_data = pd.DataFrame()

    url = yes24_year_url.format(year, month, page)
    response = urllib.request.urlopen(url)
    soup = bs(response, 'html.parser')
    result = soup.select('td.goodsTxtInfo')
    year_date = str(year)+ str(month)

    for i, post in enumerate(result):
      try:
        rank =  soup.select_one(f'#goods{i+1+20*(page-1)}').text
        review = post.select_one('p.review > a').text
        context = post.select_one('p:nth-of-type(1)').text
        auther = post.select_one('div').text
        df = pd.DataFrame({'rank':rank,'context':context,'review':review,'auther':auther}, index = [0])
        yes24_year_data = pd.concat([yes24_year_data,df])
      except AttributeError as e:
        print(e)
        print(i)
        pass

    yes24_year_data['date'] = year_date

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='!As36190301',
                            db='yoyoyo',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:!As36190301@localhost/yoyoyo')
    yes24_year_data.to_sql('yes24_year',if_exists = 'append', con = engine)
    con.commit()

if __name__ == "__main__":

    for i in range(1, 5450):

        a = datetime.datetime(2008, 1, 1) + datetime.timedelta(days= i - 1)
        print(i,a)

        for k in range(1,11):

          yes24_year(a.strftime("%Y"),a.strftime("%m"),k)
          yes24_day(a.strftime("%Y"),a.strftime("%m"),a.strftime("%d"),k )

          for j in range(1,6):
            
            yes24_week(a.strftime("%Y"),a.strftime("%m"),j,k)       


