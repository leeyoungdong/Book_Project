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
#C:\Users\kreuz\Downloads\data\data
# chosun = pd.read_csv('C:/Users/youngdong/Desktop/data/chosun_news_202211211723.csv')
donga = pd.read_csv('C:/Users/kreuz/Downloads/data/data/donga_news_202211221448.csv')
hani = pd.read_csv('C:/Users/kreuz/Downloads/data/data/hani_news_202211262344.csv')

#print(donga)
#print(donga.index.tolist())
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

def listEmpty(x):
    if len(x)== 0:
        y =" "
        return y
    else :
        y =" ".join(x)
        return y

def df_sep(df, table):
    DATE =pd.DataFrame()
    # con = connet()
    # cursor = con.cursor()
    # a = f"""select count(*) from project.{table};"""
    # b = cursor.execute(a)
    # c = cursor.fetchone()[0]
    # print(c)
    base = pd.DataFrame(df)
    base = base.reset_index()
    news_table = pd.DataFrame()
    CONTEXT = pd.DataFrame()
    # base = base.apply(lambda x: index_key(x['company'],c), axis =1)
    base['index'] = base['index'] + base.index.tolist()
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
    print(DATE)
    #df_to_db(CONTEXT, 'CONTEXT')
    #df_to_db(DATE, 'DATE')
    #df_to_db(news_table, 'news_table')    

df_sep(donga_new(donga), 'donga_news')