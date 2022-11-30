import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
from news_eda import donga_new, joongang_new, hani_new, chosun_new, khan_new
from konlpy.tag import Okt
from collections import Counter
import re
import konlpy
from konlpy.tag import Okt
from konlpy.utils import pprint
from collections import Counter
okt = Okt()
#from stopword import chosun_col, joongang_col, hani_col, khan_col, donga_col


chosun_col = ['z','index','0','date']
joongang_col = ['z','index','context','date']
hani_col = ['z','index','category','title','pdate']
khan_col = ['z','index','context','date']
donga_col = ['z','index', '0','date']
#db connect
def connet():
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='0000',
                        db='project',
                        charset='utf8')
    return con

def df_to_db(df, table):
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='0000',
                        db='project2',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:0000@localhost/project2')
    df.to_sql(f'{table}',if_exists = 'append', con = engine)
    con.commit()
    con.close()

# base.apply(lambda x: index_key(x['company'],c), axis =1)
# def custom(x)
#    if '' in  x:
#       return Unknown
#    else:
#     return x

# df.apply(lambda x: custom(x["SUBJECT"]), axis = 1)

"""
date 칼럼 format
조 2000-20-20 date
중 2020.20.20 00:00 date
동 20002020 date
경 20202020 date
한 등록 :2020-20-20 00: pdage
"""
#자연어처리부분


#불용어 사전 - 파일첨부해놓음
#자연어처리한 부분이 현재 분석에 필요하지않아 
#따로 사용 안하는 중이지만 일단은 드립니다





#함수 아래 첫줄 자연어 처리할부분 타이틀변수에 저장해서 사용
#46번 줄 참고하쉐요

def get_nouns(x):
    nouns_tagger = Okt()
    nouns = nouns_tagger.nouns(x)
    #EDA\stopwords.txt
    with open('EDA\stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = f.readlines()
    stopwords = [x.strip() for x in stopwords]

    # 한글자 키워드 제거합니다
    nouns = [noun for noun in nouns if len(noun)>1]

    #불용어를 제거합니다
    nouns = [noun for noun in nouns if noun not in stopwords]

    return nouns

def db_to_df(table ,column, year, month, day,eda ,col):

    con = connet()
    cursor = con.cursor()
# project.  ---- db 이름
    sql = f"""select * from project.{table}
              where {column} like '%{year}%%{month}%%{day}%'"""
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #joongang_col = ['z','index','context','date']
    print(result)
    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['z'], axis= 1)
    
    eda(a)
    #print(a)
    return eda(a)


def listEmpty(x):
    if len(x)== 0:
        y =" "
        return y
    else :
        y =" ".join(x)
        return y

def df_sep(df, table):
    DATE =pd.DataFrame()
    con = connet()
    cursor = con.cursor()
    a = f"""select count(*) from project.{table};"""
    b = cursor.execute(a)
    c = cursor.fetchone()[0]
    print(c)
    base = pd.DataFrame(df)
    base = base.reset_index()
    news_table = pd.DataFrame()
    CONTEXT = pd.DataFrame()
    # base = base.apply(lambda x: index_key(x['company'],c), axis =1)
    base['index'] = base['index'] + c
    base['index'] = base['index'].astype(str)
    #base['index'] = base['company'].apply(lambda x: index_key(x['company']))
    base['date'] = pd.to_datetime(base['date'])
    base['year'] = base['date'].dt.year
    base['month']= base['date'].dt.month
    base['day']= base['date'].dt.day
    DATE = base[['year','month', 'day']]
    #item키 생성 방식
    base['cc']= base['company'].str[:1]

    base['index'] = base['index']+ base['cc']
    #이 item 키를 가지고 news_table과 DATE를 만듬
    DATE['index'] = base['index']
    news_table['context']= base['title']
    news_table['index']= base['index']
    base['title_nouns']= base['title'].apply(lambda x: get_nouns(x))
    CONTEXT['context']=base['title']
    #CONTEXT['word_one'] = base['title_nouns']
    base['title_noun_text']=  base['title_nouns'].apply(lambda x : listEmpty(x))
    CONTEXT['word_one']= base['title_noun_text']
    if(table == 'hani_news'):
        CONTEXT['category']= base['category']
    else:
        CONTEXT['category']= " "
    print(CONTEXT)
    df_to_db(CONTEXT, 'CONTEXT')
    df_to_db(DATE, 'DATE')
    df_to_db(news_table, 'news_table')    


    # else : # title date company category
# def df_temp(df, table):
#     DATE =pd.DataFrame()
#     con = connet()
#     cursor = con.cursor()
#     a = f"""select count(*) from project.{table};"""
#     b = cursor.execute(a)
#     c = cursor.fetchone()[0]
#     #print(c)
#     base = pd.DataFrame(df)
#     base['title_nouns']= base['title'].apply(lambda x: get_nouns(x))
#     print(base)

#df_temp(db_to_df('donga_news','date','2022','10','29', donga_new, donga_col),'donga_news')
   
df_sep(db_to_df('donga_news','date','2022','10','29', donga_new, donga_col),'donga_news')
#  donga_new, joongang_new, hani_new, chosun_new, khan_new 
#print(db_to_df('donga_news','date','2022','10','29', donga_new, donga_col))# title date company
#print(db_to_df('joongang_news','date','2022','10','29', joongang_new, joongang_col))#title date   company
#print(db_to_df('hani_news','pdate','2022','10','29', hani_new, hani_col))# title date company category
# print(db_to_df('chosun_news','date','2022','10','29', chosun_new, chosun_col))# title date company
# print(db_to_df('khan_news','date','2022','10','29', khan_new, khan_col))#title date company



