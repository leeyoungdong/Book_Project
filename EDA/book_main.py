import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
from book_eda import ip_grade, ip_m_info, ip_sales, ip_y_info, kyobo_dup
from book_columns import 

#db connect
def connet():
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project',
                        charset='utf8')
    return con

def df_to_db(df, table):
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project2',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:0000@localhost/project4')
    df.to_sql(f'{table}',if_exists = 'append', con = engine)
    con.commit()
    con.close()

"""
데이터에 적재 되어있는 Table 
interpark_month_grade/info/sales
column - 0 / index/ 21 / 30 /date - 0 / index / 3 /5 /15 /51 /186/187/date/rank - 0 / index /315 /319 /date
interpark_year_grade/info/sales(2020)
column - 0 / index/ 21 / 30 /date - 0 / index / 3 /5 /15 /51 /186/187/date/rank - 0 / index /315 /319 /date
jongang_isbn
column -
kb_monthly(202012)/weekly(2020205)/yearly(2020)
column - index / 0 / 기간 카테고리/ 순위 / 제목 / 저자 / 출판사 /출판연도 /평점 / 리뷰개수
yes24_day(2020-12-31)/week(2020125)/year(202012)
column - 0 / index /b_rank / context / rewiew / auther /r_date
"""

def db_to_df(table ,column, year, month, day, eda ,col):

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
 
