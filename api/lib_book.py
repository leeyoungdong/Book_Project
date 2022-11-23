import time
import urllib
import json
import requests
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
from key_value import joongang_lib_key

jongang_lib_url = 'https://www.nl.go.kr/NL/search/openApi/search.do?key={}&apiType=xml&detailSearch=true&category={}&sort=&pageNum={}&pageSize=100'

def jongang_api(category, page):

    jongang_data = pd.DataFrame()

    word = urllib.parse.quote(category)
    url = jongang_lib_url.format(joongang_lib_key, word, page)
    result = requests.get(url)
    soup = bs(result.text,'lxml-xml')
    print(result)
    # print("total book list [%s] " % soup.find('total').text)

    get = soup.find_all("item")

    for lib in get:
        title = lib.find("title_info").get_text()
        author = lib.find("author_info").get_text()
        pub = lib.find("pub_info").get_text()
        pub_year = lib.find('pub_year_info').get_text()
        type_name = lib.find('kdc_name_1s').get_text()

        df = pd.DataFrame({"title":title,
                           "author":author,
                           "pub_year":pub_year,
                           "pub":pub,
                           "type_name":type_name}, index = [0])

        jongang_data = pd.concat([jongang_data, df])

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    jongang_data.to_sql('jongang_lib_data',if_exists = 'append', con = engine)
    con.commit()

if __name__ == '__main__':

    for i in range(1, 48392):
        print(i)
        jongang_api('도서', i)