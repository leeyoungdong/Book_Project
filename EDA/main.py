import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
from news_eda import donga_new, joongang_new, hani_new, chosun_new, khan_new
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
                        db='project4',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:0000@localhost/project4')
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
    print(a)
    return eda(a)
 
# def df_sep(df, table):
#     DATE =pd.DataFrame()
#     con = connet()
#     cursor = con.cursor()
#     a = f"""select count(*) from project3.{table};"""
#     b = cursor.execute(a)
#     c = cursor.fetchone()[0]
#     print(c)
#     base = pd.DataFrame(df)
#     base = base.reset_index()
#     # base = base.apply(lambda x: index_key(x['company'],c), axis =1)
#     base['index'] = base['index'] + c
#     base['index']= base['index'].astype(str)
#     #base['index'] = base['company'].apply(lambda x: index_key(x['company']))

#     DATE = base[['year','month', 'day']]
#     # base['index'] = base['index'] + 'j'
#     # print( base['company'][0] )
#     # if 'joongang' in base['company']:
#     #     base['index'] = base['index'] + c + str('j')
#     # elif base['company'] == 'donga':
#     #     base['index'] = base['index'] + c + str('d')
#     # elif base['company'] == 'chosun':
#     #     base['index'] = base['index'] + c + str('c')
#     # elif base['company'] == 'khan':
#     #     base['index'] = base['index'] + c + str('k')
#     # else:
#     #     base['index'] = base['index'] + c + str('h')
#     # print(base)
#     # if len(base.columns) > 3: # title date company
#     #     base =

#     # else : # title date company category
        
        

#df_sep(db_to_df('donga_news','date','2022','10','29', donga_new, donga_col),'donga_news')
#  donga_new, joongang_new, hani_new, chosun_new, khan_new 
print(db_to_df('donga_news','date','2022','10','29', donga_new, donga_col))# title date company
#print(db_to_df('joongang_news','date','2022','10','29', joongang_new, joongang_col))#title date   company
# print(db_to_df('hani_news','pdate','2022','10','29', hani_new, hani_col))# title date company category
# print(db_to_df('chosun_news','date','2022','10','29', chosun_new, chosun_col))# title date company
# print(db_to_df('khan_news','date','2022','10','29', khan_new, khan_col))#title date company