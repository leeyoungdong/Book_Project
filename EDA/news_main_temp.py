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

# 형태소 분리기
okt = Okt()

"""
date 칼럼 format
조 2000-20-20 date
중 2020.20.20 00:00 date
동 20002020 date
경 20202020 date
한 등록 :2020-20-20 00: pdage
"""

def df_to_db(df, table):
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project2',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    df.to_sql(f'{table}',if_exists = 'append', con = engine)
    con.commit()
    # con.close()

def connet():
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project3',
                        charset='utf8')
    return con


def get_nouns(x):
    nouns_tagger = Okt()
    nouns = nouns_tagger.nouns(x)
    #EDA\stopwords.txt
    with open('C:/Users/youngdong/Book_Project/eda/stopwords.txt', 'r', encoding='utf-8') as f:
        stopwords = f.readlines()
    stopwords = [x.strip() for x in stopwords]

    # 한글자 키워드 제거합니다
    nouns = [noun for noun in nouns if len(noun)>1]

    #불용어를 제거합니다
    nouns = [noun for noun in nouns if noun not in stopwords]

    return nouns

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
    a = f"""select count(*) from project2.news_table_daily;"""
    b = cursor.execute(a)
    c = cursor.fetchone()[0]

    base = pd.DataFrame(df)
    base = base.reset_index()
    news_table = pd.DataFrame()
    CONTEXT = pd.DataFrame()
    # base = base.apply(lambda x: index_key(x['company'],c), axis =1)
    #base = base.reset_index()
    base['index'] = base.index + c
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
    CONTEXT['news_publisher']= base['company']
    #CONTEXT['word_one'] = base['title_nouns']
    base['title_noun_text']=  base['title_nouns'].apply(lambda x : listEmpty(x))
    CONTEXT['word_one']= base['title_noun_text']
    if(table == 'hani_news'):
        CONTEXT['category']= base['category']
    else:
        CONTEXT['category']= " "
    print(DATE)
    df_to_db(CONTEXT, 'context_daily')
    df_to_db(DATE, 'date_daily')
    df_to_db(news_table, 'news_table_daily')
    
def dropNull(df):
    df = df.dropna(subset=['title'])
    return df

if __name__ == "__main__":
    # 뉴스 입력값 구조
    # df = dropNull(donga_new(donga))
    # df_sep(df, 'donga_news') 
    print('c')
