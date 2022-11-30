import pandas as pd
import numpy as np
import re
import pymysql
from sqlalchemy import create_engine

jongang_isbn = pd.read_csv('C:/Users/youngdong/Desktop/data/joongdo_notyet.csv')

lib_table = pd.DataFrame()
lib_pub = pd.DataFrame()
lib_sa = pd.DataFrame()
lib_info = pd.DataFrame()

a = jongang_isbn.groupby('author').cumcount()+1
jongang_isbn['new'] = a
jongang_isbn['new'] = jongang_isbn['new'].astype('str')
jongang_isbn['author'] = jongang_isbn['author'] + jongang_isbn['new']

b = jongang_isbn.groupby('title').cumcount()+1
jongang_isbn['new1'] = b
jongang_isbn['new1'] = jongang_isbn['new1'].astype('str')
jongang_isbn['title'] = jongang_isbn['title'] + jongang_isbn['new1']

c = jongang_isbn.groupby('pub').cumcount()+1
jongang_isbn['new2'] = c
jongang_isbn['new2'] = jongang_isbn['new2'].astype('str')
jongang_isbn['pub'] = jongang_isbn['pub'] + jongang_isbn['new2']

lib_table = jongang_isbn[['title','author','pub']]
lib_pub = jongang_isbn[['pub','repub','pub_year','pub_month','pub_day']]
lib_sa = jongang_isbn[['author','ebook','price','SUBJECT']]
lib_info = jongang_isbn[['title','isbn','isbn_add_code']]


engine = create_engine('mysql+pymysql://root:lgg032800@localhost/project2')
    
con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project2',
                        charset='utf8')

lib_table.to_sql('lib_table',if_exists = 'append', con = engine)
con.commit()

lib_pub.to_sql('lib_pub',if_exists = 'append', con = engine)
con.commit()

lib_sa.to_sql('lib_sa',if_exists = 'append', con = engine)
con.commit()

lib_info.to_sql('lib_info',if_exists = 'append', con = engine)
con.commit()