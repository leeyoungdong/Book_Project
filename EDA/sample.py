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
from news_eda import donga_new

donga_URL = 'https://www.donga.com/news/Pdf?ymd={}'

def donga(date):

    donga_data = pd.DataFrame()
    url = donga_URL.format(date)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    result = soup.select('div.section_txt')

    for post in result:
        try:
            context = post.select_one('ul.desc_list').text
            con = context.split('\r')
            df = pd.DataFrame(con)
            donga_data = donga_data.append(df, ignore_index = True)

        except AttributeError as e:
            print(e)
            pass
    
    donga_data['date'] = str(date)
    print(donga_data)
    donga_new(donga_data)
    return donga_data
    

donga(20221021)

# if __name__ == '__main__':

#     for i in range(7133, 8361):
#             print(i)
#             a = datetime.datetime(2000, 1, 1) + datetime.timedelta(days= i - 1)
#             donga(a.strftime("%Y%m%d"))

# a = datetime.datetime(2000, 1, 1) + datetime.timedelta(days= 1 - 1)
# donga(a.strftime("%Y%m%d"))
