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
import json
from dateutil.relativedelta import relativedelta

f= pd.DataFrame()
total =pd.DataFrame()

def preprocess_sentence(sentence):
  try:
    sentence = sentence.lower().strip() 
    sentence = re.sub(r"[a-zA-Z]"," ", sentence)
    return sentence
  except: pass

def presub(sentence):
  sentence = re.sub(r"[-=+,#/\?:^.@*\"※~ㆍ!]", "", sentence)
  return sentence


def interpark_year(year, page):

    url = f'http://book.interpark.com/display/collectlist.do?_method=bestsellerHourNewYearList201605_xml&cltTp=82&cltWeek={year}000&category=year&bestTp=1&dispNo=028&clickCnb=Y&page={page}'
    print(url)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    result = soup.text

    # print(result)z
    a = soup.select("span")
    json_result = json.loads(json.dumps(result))
    json_result = re.sub("\"", "", json_result)
    a = pd.DataFrame([json_result.split('\n')], columns=['1','2','3','4','5','6'])
    # a = a.replace(str('/'),' ')
    b = json.dumps(a['5'].to_json())
    b = pd.DataFrame([b.split('{')])
    c = b.iloc[0][3:48]
    d = pd.DataFrame(c)
    d.columns = ['1']

    e = d['1'].str.split(':', expand= True)
    e.columns = ['{}'.format(x+1) for x in e.columns]

    g = e.iloc[0:15]
    h = e.iloc[15:30]
    i = e.iloc[31:48]
    g = g[['3','5','15','51','186','187']]
    h = h[['315','319']]
    i = i[['21','30']]

    g['3'] =  g['3'].apply(preprocess_sentence)
    g['5'] =   g['5'].apply(preprocess_sentence)
    g['187'] =  g['187'].apply(preprocess_sentence)
    g['187'] =  g['187'].apply(presub)
    g.sort_values('187')

    g['15'] = g['15'].str.replace(',', "' ")
    g['15'] = g['15'].str.replace(r'\\\\', r'\\')
    g['15'] = "'" + g['15'].astype(str)
    g['15'] = g['15'].str.decode('unicode_escape')
    g['15'] = g['15'].apply(preprocess_sentence) 


    g['51'] = g['51'].str.replace(',', "' ")
    g['51'] = g['51'].str.replace(r'\\\\', r'\\')
    g['51'] = "'" + g['51'].astype(str)
    g['51'] = g['51'].str.decode('unicode_escape')
    g['51'] = g['51'].apply(preprocess_sentence) 

    g['186'] = g['186'].str.replace(',', "' ")
    g['186'] = g['186'].str.replace('.', "' ")
    g['186'] = g['186'].str.replace(r'\\\\', r'\\')
    g['186'] = "'" + g['186'].astype(str)
    g['186'] = g['186'].str.decode('unicode_escape')
    g['186'] = g['186'].apply(preprocess_sentence)

    g['15'] = g['15'].str.replace(',', "' ")
    g['15'] = g['15'].str.replace(r'\\\\', r'\\')
    g['15'] = "'" + g['15'].astype(str)

    i['21']= i['21'].apply(presub)
    i['21']= i['21'].apply(preprocess_sentence)
    i['30']= i['30'].apply(preprocess_sentence)

    h['315'] = h['315'].apply(preprocess_sentence)
    h['319'] = h['319'].apply(preprocess_sentence)
    h['319'] = h['319'].apply(presub)

    
    g['date'], h['date'], i['date'] = str(year), str(year), str(year)
    g['rank'] = [(x + 1 +(page - 1) * 15) for x in range(15)]

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    i.to_sql('interpark_year_grade',if_exists = 'append', con = engine)
    con.commit()

    g.to_sql('interpark_year_info',if_exists = 'append', con = engine)
    con.commit()

    h.to_sql('interpark_year_sales',if_exists = 'append', con = engine)
    con.commit()


def interpark_month(year,month, page):

    url = f'https://book.interpark.com/display/collectlist.do?_method=bestsellerHourNewMonthList201605_xml&cltTp=28&cltWeek={year}{month}0&category=month&bestTp=1&dispNo=028037&clickCnb=Y&page={page}'
    print(url)
    response = urllib.request.urlopen(url)
    soup = bs(response,'html.parser')
    result = soup.text

    # print(result)z
    a = soup.select("span")
    json_result = json.loads(json.dumps(result))
    json_result = re.sub("\"", "", json_result)
    a = pd.DataFrame([json_result.split('\n')], columns=['1','2','3','4','5','6'])
    # a = a.replace(str('/'),' ')
    b = json.dumps(a['5'].to_json())
    b = pd.DataFrame([b.split('{')])
    c = b.iloc[0][3:48]
    d = pd.DataFrame(c)
    d.columns = ['1']

    e = d['1'].str.split(':', expand= True)
    e.columns = ['{}'.format(x+1) for x in e.columns]

    g = e.iloc[0:15]
    h = e.iloc[15:30]
    i = e.iloc[31:48]
    g = g[['3','5','15','51','186','187']]
    h = h[['315','319']]
    i = i[['21','30']]

    g['3'] =  g['3'].apply(preprocess_sentence)
    g['5'] =   g['5'].apply(preprocess_sentence)
    g['187'] =  g['187'].apply(preprocess_sentence)
    g['187'] =  g['187'].apply(presub)
    g.sort_values('187')

    g['15'] = g['15'].str.replace(',', "' ")
    g['15'] = g['15'].str.replace(r'\\\\', r'\\')
    g['15'] = "'" + g['15'].astype(str)
    g['15'] = g['15'].str.decode('unicode_escape')
    g['15'] = g['15'].apply(preprocess_sentence) 


    g['51'] = g['51'].str.replace(',', "' ")
    g['51'] = g['51'].str.replace(r'\\\\', r'\\')
    g['51'] = "'" + g['51'].astype(str)
    g['51'] = g['51'].str.decode('unicode_escape')
    g['51'] = g['51'].apply(preprocess_sentence) 

    g['186'] = g['186'].str.replace(',', "' ")
    g['186'] = g['186'].str.replace('.', "' ")
    g['186'] = g['186'].str.replace(r'\\\\', r'\\')
    g['186'] = "'" + g['186'].astype(str)
    g['186'] = g['186'].str.decode('unicode_escape')
    g['186'] = g['186'].apply(preprocess_sentence)

    g['15'] = g['15'].str.replace(',', "' ")
    g['15'] = g['15'].str.replace(r'\\\\', r'\\')
    g['15'] = "'" + g['15'].astype(str)

    i['21']= i['21'].apply(presub)
    i['21']= i['21'].apply(preprocess_sentence)
    i['30']= i['30'].apply(preprocess_sentence)

    h['315'] = h['315'].apply(preprocess_sentence)
    h['319'] = h['319'].apply(preprocess_sentence)
    h['319'] = h['319'].apply(presub)

    
    g['date'], h['date'], i['date'] = str(year)+str(month), str(year)+str(month),str(year)+ str(month)
    g['rank'] = [(x + 1 +(page - 1) * 15) for x in range(15)]

    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    i.to_sql('interpark_month_grade',if_exists = 'append', con = engine)
    con.commit()

    g.to_sql('interpark_month_info',if_exists = 'append', con = engine)
    con.commit()

    h.to_sql('interpark_month_sales',if_exists = 'append', con = engine)
    con.commit()


        # for k in range(1,11):

        #   yes24_year(a.strftime("%Y"),a.strftime("%m"),k)
        #   yes24_day(a.strftime("%Y"),a.strftime("%m"),a.strftime("%d"),k )

        #   for j in range(1,6):
            
        #     yes24_week(a.strftime("%Y"),a.strftime("%m"),j,k)    /
if __name__ == "__main__":


  for z in range(1, 17):

      for k in range(1,13):
        a = datetime.datetime(2008, 2, 1) + relativedelta(months=k)
        
        for q in range(1,11):
          print(a.strftime("%m"), z)
          interpark_month(2006+z, a.strftime("%m"), q)