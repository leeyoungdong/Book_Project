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

jongurl = 'https://www.nl.go.kr/seoji/SearchApi.do?cert_key=d8b083a071d52098f7ebc90f64ae6cb9bc66a6c47f0a6d10c4fd1f0bd5907c5c&result_style=xml&page_no={}&page_size=100'

def jongang_api(page):

    jongang_data = pd.DataFrame()

    url = jongurl.format( page)
    result = requests.get(url).text
    soup = bs(result,'lxml-xml')

    get = soup.find_all("e")

    for post in get:
      TITLE = post.find("TITLE").get_text()
      PUBLISHER = post.find("PUBLISHER").get_text()
      AUTHOR = post.find("AUTHOR").get_text()
      EDITION_STMT = post.find("EDITION_STMT").get_text()
      PRE_PRICE = post.find("PRE_PRICE").get_text()
      EA_ADD_CODE = post.find("EA_ADD_CODE").get_text()
      EBOOK_YN = post.find("EBOOK_YN").get_text()
      EA_ISBN = post.find("EA_ISBN").get_text()
      SUBJECT = post.find("SUBJECT").get_text()
      PUBLISH_PREDATE = post.find("PUBLISH_PREDATE").get_text()

      df = pd.DataFrame({"title":TITLE,
                           "author":AUTHOR,
                           "pub_year":PUBLISH_PREDATE,
                           "pub":PUBLISHER,
                           "isbn_add_code":EA_ADD_CODE,
                           "repub":EDITION_STMT,
                           "isbn":EA_ISBN,
                           "ebook":EBOOK_YN,
                           "price":PRE_PRICE,
                           "pub":PUBLISHER,
                           "SUBJECT":SUBJECT}, index = [0])
      
      jongang_data = pd.concat([jongang_data, df])
    
    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='!As36190301',
                            db='yoyoyo',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:!As36190301@localhost/yoyoyo')
    jongang_data.to_sql('jongang_isbn',if_exists = 'append', con = engine)
    con.commit()

if __name__ == '__main__':
  for i in range(1,44396):

      print(i)
      jongang_api(i)
    
