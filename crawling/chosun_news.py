import time
import urllib
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import datetime
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from urllib.request import HTTPError

chosun_URL = 'https://archive.chosun.com/pdf/i_service/index_new_s.jsp?Y={}&M={}&D={}'

def chosun_crawl(year, month, day):

    chosun_data = pd.DataFrame()
    #LeftContent > div:nth-child(11)
    url = chosun_URL.format(year, month, day)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    context_results = soup.select("div.ss_arti_tit")

    for get in context_results: 
        context = get.select_one('div.ss_list').text
        con = context.split('\n')
        df = pd.DataFrame(con)
        chosun_data = chosun_data.append(df, ignore_index = True)

    news_date = datetime.date(year, month, day)
    
    day_results = soup.select('#LeftContent')
    for got in day_results:
        date = got.select('div.ss_txt')
    chosun_data.replace('', np.nan, inplace=True)
    chosun_data = chosun_data.dropna()
    chosun_data = chosun_data.reset_index()
    chosun_data = chosun_data.drop(columns='index')
    chosun_data['date'] = news_date
    print(chosun_data)    
    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    chosun_data.to_sql('chosun_news',if_exists = 'append', con = engine)
    con.commit()

if __name__ == '__main__':
    
    try:
        for m in range(1,23):

            for i in range(1,13):
            
                if (i == 1)|(i == 3)|(i == 5)|(i == 7)|(i == 8)|(i == 10)|(i == 12):
                    for j in range(1,32):
                        chosun_crawl(2000+m,i,j)
                        print(i,j,m)

                elif i == 2: 
                    for k in range(1,29):
                        chosun_crawl(2000+m,i,k)
                        print(i,k,m)

                else:
                    for x in range(1,31):
                        chosun_crawl(2000+m,i,x)
                        print(i,x,m)

    except HTTPError as e:
        print(e)
        pass
