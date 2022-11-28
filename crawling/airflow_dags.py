# from airflow.models import DAG
# from airflow.utils.dates import days_ago
# from airflow.operators.bash import BashOperator
# from airflow.operators.python import PythonOperator
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import pymysql
import os
import re
from sqlalchemy import create_engine
import time
from pprint import pprint
from datetime import datetime


# args = {'owner':'youngdong'}

# dag = DAG(dag_id = 'sample_Batch',
#           default_args=args,
#           start_date= datetime(22, 11, 27),
#           catchup= False,
#           description= ' pipe line batch process',
#           schedule_interval = '* * * * *'
#           )

# now_day = datetime.now()

# my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
# a= pd.DataFrame(my_2darray)

# def sample1():
    
#     my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
#     a= pd.DataFrame(my_2darray)

#     con = pymysql.connect(host='database-1.crcwjnuinlbu.ap-northeast-2.rds.amazonaws.com',
#                       port=3306,
#                       user='admin',
#                       password='lgg032800',
#                       db='Project_Data',
#                       charset='utf8')

#     engine = create_engine('mysql+pymysql://admin:lgg032800@database-1.crcwjnuinlbu.ap-northeast-2.rds.amazonaws.com/Project_Data')
#     a.to_sql('a',if_exists = 'append', con = engine)
#     con.commit()
 
# def sample2(): 
#     my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
#     b= pd.DataFrame(my_2darray)

#     con = pymysql.connect(host='database-1.crcwjnuinlbu.ap-northeast-2.rds.amazonaws.com',
#                       port=3306,
#                       user='admin',
#                       password='lgg032800',
#                       db='Project_Data',
#                       charset='utf8')

#     engine = create_engine('mysql+pymysql://admin:lgg032800@database-1.crcwjnuinlbu.ap-northeast-2.rds.amazonaws.com/Project_Data')
#     b.to_sql('a',if_exists = 'append', con = engine)
#     con.commit()
 
    
# # def khan_daily():
# #     khan(year, month, day)
# #     now_day.strftime()
# # khan(year, month, day)
# #chosun_crawl(year, month, day)
# # hani_news(date) d
# # interpark_year(year, page)
# # donga(date)
# #  a.strftime("%Y%m%d")
# api_one = PythonOperator(
#     task_id = 'sample1',
#     python_callable = sample1,
#     dag = dag
# )

# api_two = PythonOperator(
#     task_id = 'sample2',
#     python_callable = sample2,
#     dag = dag
# )

# # api_three = PythonOperator(
# #     task_id = 'dart_daily',
# #     python_callable = dart_daily,
# #     dag = dag 
# # )

# api_one >> api_two
# # api_one >> api_two >> api_three

my_2darray = [[1, 2, 3], [4, 5, 6]]
a= pd.DataFrame(my_2darray)
print(a)