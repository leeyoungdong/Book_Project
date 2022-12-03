import pandas as pd
import numpy as np
import re
import pymysql
from sqlalchemy import create_engine
from book_eda import *

def dup_count(table, column):
    a = table.groupby(f'{column}').cumcount()+1
    table['new1'] = a
    table['new1'] = table['new1'].astype('str')
    table[f'{column}'] = table[f'{column}'] + '/' +table['new1']
    return table[f'{column}']
####################
def kb_m():


    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = pd.read_csv('C:/Users/youngdong/Desktop/data/kb_monthly.csv')
    kb_m = pd.DataFrame(kyobo_dup(kb_m))

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'k'+'m'


    kb_m['저자'] = dup_count(kb_m, '저자')
    kb_m['저자'] = kb_m['저자'] .astype('str')
    kb_m['저자']  = kb_m['저자']  + 'k'+'m'
    kb_m['제목'] = kb_m['제목'].str.upper()
    kb_m['제목'] = dup_count(kb_m, '제목')
    kb_m['제목'] = kb_m['제목'].astype('str')
    kb_m['제목'] = kb_m['제목']  + kb_m['index']
    # period end
    # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['기간'] = kb_m['기간'].astype('str')
    kb_m['기간'] = kb_m['기간'] + 'k'
    kb_m['기간'] = dup_count(kb_m, '기간')
    period['date'] = kb_m['기간'] 
    period['pub_date'] = kb_m['출판연도']
    period['year'] = kb_m['기간'].str.slice(0,4)
    period['month'] = kb_m['기간'].str.slice(4,6)
    # period['week'] = kb_m['wperiod'].str.slice(6,7)
    #table end
    # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['기간']
    book_table['title'] = kb_m['제목']
    book_table['author'] = kb_m['저자']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['제목']
    # information['context'] = kb_m['description']
    information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['출판사']
    # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['순위']
    reputation['review_num'] = kb_m['리뷰개수']
    reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'kyobo'+'m'
    reputation['portal'] = dup_count(reputation, 'portal')

    # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    buyc['portal'] = dup_count(buyc, 'portal')
    buyc = buyc.drop('new1',axis=1)

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
####################
def kb_w():

    kb_w = pd.read_csv('C:/Users/youngdong/Desktop/data/kb_weekly.csv')
    kb_m = pd.DataFrame(kyobo_dup(kb_w))


    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])




    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'k'+ 'w'


    kb_m['저자'] = dup_count(kb_m, '저자')
    kb_m['저자'] = kb_m['저자'] .astype('str')
    kb_m['저자']  = kb_m['저자']  + 'k' + 'w'
    kb_m['제목'] = kb_m['제목'].str.upper()
    kb_m['제목'] = dup_count(kb_m, '제목')
    kb_m['제목'] = kb_m['제목'].astype('str')
    kb_m['제목'] = kb_m['제목'] + kb_m['index']
    # period end
    # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['기간'] = kb_m['기간'].astype('str')
    kb_m['기간'] = kb_m['기간'] + 'k'+ 'w'
    kb_m['기간'] = dup_count(kb_m, '기간')
    period['date'] = kb_m['기간'] 
    period['pub_date'] = kb_m['출판연도']
    period['year'] = kb_m['기간'].str.slice(0,4)
    period['month'] = kb_m['기간'].str.slice(4,6)
    period['week'] = kb_m['기간'].str.slice(6,7)
    #table end
    # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['기간']
    book_table['title'] = kb_m['제목']
    book_table['author'] = kb_m['저자']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['제목']
    # information['context'] = kb_m['description']
    information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['출판사']
    # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['순위']
    reputation['review_num'] = kb_m['리뷰개수']
    reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'kyobo'+ 'w'
    reputation['portal'] = dup_count(reputation, 'portal')

    # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    buyc['portal'] = dup_count(buyc, 'portal')
    buyc = buyc.drop('new1',axis=1)

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
#####################
def kb_y():

    kb_y = pd.read_csv('C:/Users/youngdong/Desktop/data/kb_yearly.csv')
    kb_m = pd.DataFrame(kyobo_dup(kb_y))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'k'+'y'


    kb_m['저자'] = dup_count(kb_m, '저자')
    kb_m['저자'] = kb_m['저자'] .astype('str')
    kb_m['저자']  = kb_m['저자']  + 'k'+'y'
    kb_m['제목'] = kb_m['제목'].str.upper()
    kb_m['제목'] = dup_count(kb_m, '제목')
    kb_m['제목'] = kb_m['제목'].astype('str')
    kb_m['제목'] = kb_m['제목']  + kb_m['index']
    # period end
    # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['기간'] = kb_m['기간'].astype('str')
    kb_m['기간'] = kb_m['기간'] + 'k'+ 'y'
    kb_m['기간'] = dup_count(kb_m, '기간')
    period['date'] = kb_m['기간'] 
    period['pub_date'] = kb_m['출판연도']
    period['year'] = kb_m['기간'].str.slice(0,4)
    # period['month'] = kb_m['기간'].str.slice(4,6)
    # period['week'] = kb_m['기간'].str.slice(6,7)
    #table end
    # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['기간']
    book_table['title'] = kb_m['제목']
    book_table['author'] = kb_m['저자']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['제목']
    # information['context'] = kb_m['description']
    information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['출판사']
    # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['순위']
    reputation['review_num'] = kb_m['리뷰개수']
    reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'kyobo' + 'y'
    reputation['portal'] = dup_count(reputation, 'portal')

    # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    buyc['portal'] = dup_count(buyc, 'portal')
    buyc = buyc.drop('new1',axis=1)

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def yes_d():

    yes_d = pd.read_csv('C:/Users/youngdong/Desktop/data/new_yes24_day_202211271547.csv')
    kb_m = pd.DataFrame(yes_def(yes_d))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'y'+'d'


    kb_m['auther'] = dup_count(kb_m, 'auther')
    kb_m['auther'] = kb_m['auther'] .astype('str')
    kb_m['auther']  = kb_m['auther'] + 'y'+'d'
    kb_m['context'] = kb_m['context'].str.upper()
    kb_m['context'] = dup_count(kb_m, 'context')
    kb_m['context'] = kb_m['context'].astype('str')
    kb_m['context'] = kb_m['context']  + kb_m['index']
    print(kb_m.columns)
    # # period end
    # # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['r_date'] = kb_m['r_date'].astype('str')
    kb_m['r_date'] = kb_m['r_date']+'y' + 'd'
    kb_m['r_date'] = dup_count(kb_m, 'r_date')
    period['date'] = kb_m['r_date']
    period['pub_date'] = kb_m['publication']
    period['year'] = kb_m['r_date'].str.slice(0,4)
    period['month'] = kb_m['r_date'].str.slice(5,7)
    period['day'] = kb_m['r_date'].str.slice(8,10)
    # #table end
    # # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['r_date']
    book_table['title'] = kb_m['context']
    book_table['author'] = kb_m['auther']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['context']
    # information['context'] = kb_m['description']
    # information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['publisher']
    # # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['b_rank']
    reputation['review_num'] = kb_m['review']
    # reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'yes' + 'd'
    reputation['portal'] = dup_count(reputation, 'portal')

    # # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def yes_m():

    yes_m = pd.read_csv('C:/Users/youngdong/Desktop/data/new_yes24_week_202211271547.csv')
    kb_m = pd.DataFrame(yes_def(yes_m))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'y'+'m'


    kb_m['auther'] = dup_count(kb_m, 'auther')
    kb_m['auther'] = kb_m['auther'] .astype('str')
    kb_m['auther']  = kb_m['auther'] + 'y'+'m'
    kb_m['context'] = kb_m['context'].str.upper()
    kb_m['context'] = dup_count(kb_m, 'context')
    kb_m['context'] = kb_m['context'].astype('str')
    kb_m['context'] = kb_m['context'] + kb_m['index']
    print(kb_m.columns)
    # # period end
    # # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['r_date'] = kb_m['r_date'].astype('str')
    kb_m['r_date'] = kb_m['r_date']+'y' + 'm'
    kb_m['r_date'] = dup_count(kb_m, 'r_date')
    period['date'] = kb_m['r_date']
    period['pub_date'] = kb_m['publication']
    period['year'] = kb_m['r_date'].str.slice(0,4)
    period['month'] = kb_m['r_date'].str.slice(4,6)
    period['week'] = kb_m['r_date'].str.slice(6,7)
    # #table end
    # # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['r_date']
    book_table['title'] = kb_m['context']
    book_table['author'] = kb_m['auther']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['context']
    # information['context'] = kb_m['description']
    # information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['publisher']
    # # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['b_rank']
    reputation['review_num'] = kb_m['review']
    # reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'yes' + 'm'
    reputation['portal'] = dup_count(reputation, 'portal')

    # # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def yes_y():

    yes_y = pd.read_csv('C:/Users/youngdong/Desktop/data/new_yes24_year_202211271548.csv')
    kb_m = pd.DataFrame(yes_def(yes_y))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'y'+'y'


    kb_m['auther'] = dup_count(kb_m, 'auther')
    kb_m['auther'] = kb_m['auther'] .astype('str')
    kb_m['auther']  = kb_m['auther'] + 'y'+'y'
    kb_m['context'] = kb_m['context'].str.upper()
    kb_m['context'] = dup_count(kb_m, 'context')
    kb_m['context'] = kb_m['context'].astype('str')
    kb_m['context'] = kb_m['context'] + kb_m['index']
    print(kb_m.columns)
    # # period end
    # # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['r_date'] = kb_m['r_date'].astype('str')
    kb_m['r_date'] = kb_m['r_date']+'y' + 'y'
    kb_m['r_date'] = dup_count(kb_m, 'r_date')
    period['date'] = kb_m['r_date']
    period['pub_date'] = kb_m['publication']
    period['year'] = kb_m['r_date'].str.slice(0,4)
    period['month'] = kb_m['r_date'].str.slice(4,6)
    # period['week'] = kb_m['r_date'].str.slice(6,7)
    # #table end
    # # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['r_date']
    book_table['title'] = kb_m['context']
    book_table['author'] = kb_m['auther']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['context']
    # information['context'] = kb_m['description']
    # information['category'] = kb_m['카테고리']
    # information['isbn'] = aladin['isbn10']
    information['publisher'] = kb_m['publisher']
    # # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['b_rank']
    reputation['review_num'] = kb_m['review']
    # reputation['review_rate'] = kb_m['평점']
    reputation['portal'] = 'yes' + 'y'
    reputation['portal'] = dup_count(reputation, 'portal')

    # # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def inter_y():

    inter_y = pd.read_csv('C:/Users/youngdong/Desktop/data/new_table1_202212012228.csv')
    kb_m = pd.DataFrame(ip_month_total(inter_y))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    # kb_m['index'] = dup_count(kb_m, 'index')
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'i'+'y'
    # print(kb_m['구매력?'])
    kb_m['author'] = dup_count(kb_m, 'author')
    kb_m['author'] = kb_m['author'] .astype('str')
    kb_m['author']  = kb_m['author'] + 'i'+'y'
    kb_m['title'] = kb_m['title'].str.upper()
    kb_m['title'] = dup_count(kb_m, 'title')
    kb_m['title'] = kb_m['title'].astype('str')
    kb_m['title'] = kb_m['title'] + kb_m['index']

    # # period end
    # # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['date'] = kb_m['date'].astype('str')
    kb_m['date'] = kb_m['date']+ 'i'+'y'
    kb_m['date'] = dup_count(kb_m, 'date')
    period['date'] = kb_m['date']
    # period['pub_date'] = kb_m['publication']
    period['year'] = kb_m['date'].str.slice(0,4)
    # period['month'] = kb_m['date'].str.slice(4,6)
    # period['week'] = kb_m['r_date'].str.slice(6,7)
    # #table end
    # # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['date']
    book_table['title'] = kb_m['title']
    book_table['author'] = kb_m['author']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['title']
    # information['context'] = kb_m['description']
    information['category'] = kb_m['category']
    # information['isbn'] = aladin['isbn10']
    # information['publisher'] = kb_m['publisher']
    # # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['rank']
    # reputation['review_num'] = kb_m['review']
    reputation['review_rate'] = kb_m['review']
    reputation['portal'] = 'interpark'+'ｙ'
    reputation['portal'] = dup_count(reputation, 'portal')

    # # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    # buyc['portal'] = dup_count(buyc, 'portal')
    # buyc = buyc.drop('new1',axis=1)
    buyc['accucnt'] = kb_m['accuCnt']
    buyc['aggrcnt'] = kb_m['aggrCnt']
    # buyc['price'] = aladin['price']
    buyc['sales'] =  kb_m['구매력?']

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def inter_m():

    inter_w = pd.read_csv('C:/Users/youngdong/Desktop/data/new_table_202212012224.csv')
    kb_m = pd.DataFrame(ip_month_total(inter_w))

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    kb_m = kb_m.reset_index()
    kb_m = kb_m.drop('index', axis = 1)
    kb_m = kb_m.drop('0', axis = 1)
    kb_m = kb_m.reset_index()
    # kb_m['index'] = dup_count(kb_m, 'index')
    kb_m['index'] = kb_m['index'].astype('str')
    kb_m['index'] = kb_m['index'] + 'i'+'m'
    # print(kb_m['구매력?'])
    kb_m['author'] = dup_count(kb_m, 'author')
    kb_m['author'] = kb_m['author'] .astype('str')
    kb_m['author']  = kb_m['author'] + 'i'+'m'
    kb_m['title'] = kb_m['title'].str.upper()
    kb_m['title'] = dup_count(kb_m, 'title')
    kb_m['title'] = kb_m['title'].astype('str')
    kb_m['title'] = kb_m['title']  + kb_m['index']

    # # period end
    # # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    kb_m['date'] = kb_m['date'].astype('str')
    kb_m['date'] = kb_m['date']+ 'i'+'m'
    kb_m['date'] = dup_count(kb_m, 'date')
    period['date'] = kb_m['date']
    # period['pub_date'] = kb_m['publication']
    period['year'] = kb_m['date'].str.slice(0,4)
    period['month'] = kb_m['date'].str.slice(4,6)
    # period['week'] = kb_m['r_date'].str.slice(6,7)
    # #table end
    # # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = kb_m['index']
    book_table['date'] = kb_m['date']
    book_table['title'] = kb_m['title']
    book_table['author'] = kb_m['author']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = kb_m['title']
    # information['context'] = kb_m['description']
    information['category'] = kb_m['category']
    # information['isbn'] = aladin['isbn10']
    # information['publisher'] = kb_m['publisher']
    # # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = kb_m['index']
    reputation['rank'] = kb_m['rank']
    # reputation['review_num'] = kb_m['review']
    reputation['review_rate'] = kb_m['review']
    reputation['portal'] = 'interpark'+'m'
    reputation['portal'] = dup_count(reputation, 'portal')

    # # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    # buyc['portal'] = dup_count(buyc, 'portal')
    # buyc = buyc.drop('new1',axis=1)
    buyc['accucnt'] = kb_m['accuCnt']
    buyc['aggrcnt'] = kb_m['aggrCnt']
    # buyc['price'] = aladin['price']
    buyc['sales'] =  kb_m['구매력?']

    con = pymysql.connect(host='localhost',
                                port=3306,
                                user='root',
                                password='lgg032800',
                                db='project2',
                                charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')

    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()
######################
def aladin():

    aladin = pd.read_csv('C:/Users/youngdong/Desktop/data/alading_week_202211291619.csv')

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])

    aladin = aladin.reset_index()
    aladin = aladin.drop('index', axis = 1)
    aladin = aladin.reset_index()
    aladin['index'] = aladin['index'].astype('str')
    aladin['index'] = aladin['index'] + 'a'


    aladin['author'] = dup_count(aladin, 'author')
    aladin['author'] = aladin['author'].astype('str')
    aladin['author'] = aladin['author'] + 'a' 
    aladin['title'] = aladin['title'].str.upper()
    aladin['title'] = dup_count(aladin, 'title')
    aladin['title'] = aladin['title'].astype('str')
    aladin['title'] = aladin['title'] + aladin['index']
    # period end
    # period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])
    aladin['wperiod'] = aladin['wperiod'].astype('str')
    aladin['wperiod'] = aladin['wperiod'] + 'w'
    aladin['wperiod'] = dup_count(aladin, 'wperiod')
    period['date'] = aladin['wperiod']
    period['pub_date'] = aladin['pubDate']
    period['year'] = aladin['wperiod'].str.slice(0,4)
    period['month'] = aladin['wperiod'].str.slice(4,6)
    period['week'] = aladin['wperiod'].str.slice(6,7)
    #table end
    # book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])
    book_table['itemkey'] = aladin['index']
    book_table['date'] = aladin['wperiod']
    book_table['title'] = aladin['title']
    book_table['author'] = aladin['author']
    # information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])
    information['title'] = aladin['title']
    information['context'] = aladin['description']
    # information['category'] = aladin['title']
    information['isbn'] = aladin['isbn10']
    information['publisher'] = aladin['publisher']
    # reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])
    reputation['itemkey'] = aladin['index']
    reputation['rank'] = aladin['rank']
    # reputation['review_num'] = aladin['title']
    # reputation['review_rate'] = aladin['author']
    reputation['portal'] = 'aladin'
    reputation['portal'] = dup_count(reputation, 'portal')


    # buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])
    buyc['portal'] = reputation['portal']
    # buyc['portal'] = dup_count(buyc, 'portal')
    # buyc['accucnt'] = aladin['wperiod']
    # buyc['aggrcnt'] = aladin['title']
    buyc['price'] = aladin['price']
    buyc['sales'] =  aladin['salesPoint']


    con = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='lgg032800',
                            db='project2',
                            charset='utf8')

    engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')


    period.to_sql('period',if_exists = 'append', con = engine)
    con.commit()

    book_table.to_sql('book_table',if_exists = 'append', con = engine)
    con.commit()

    information.to_sql('information',if_exists = 'append', con = engine)
    con.commit()

    reputation.to_sql('reputation',if_exists = 'append', con = engine)
    con.commit()

    buyc.to_sql('buyc',if_exists = 'append', con = engine)
    con.commit()


if __name__ == "__main__":
    yes_d()
    yes_m()
    yes_y()
    kb_m()
    kb_w()
    kb_y()
    inter_y()
    inter_m()
    aladin()