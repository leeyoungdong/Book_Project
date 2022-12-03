import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
from book_eda import *
from book_columns import *

#db connect ########### airflow 올릴떄 바꾸기
def connet():
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='lgg032800',
                        db='project',
                        charset='utf8')
    return con
########### airflow 올릴떄 바꾸기


def base_frame():

    period = pd.DataFrame(index=range(0),columns = ['date','year','month','week','day','pub_date'])

    book_table = pd.DataFrame(index=range(0),columns = ['itemkey','date','title','author'])

    information = pd.DataFrame(index=range(0),columns = ['title','context','category','isbn','publisher'])

    reputation = pd.DataFrame(index=range(0),columns = ['itemkey','rank','review_num','review_rate','portal'])

    buyc = pd.DataFrame(index=range(0),columns = ['portal','accucnt','aggrcnt','price','sales'])




def df_to_db(period, book_table, information, reputation, buyc):

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

def db_df_day(table ,column, year, month, day, eda ,col):

    con = connet()
    cursor = con.cursor()
    # project.  ---- db 이름
    sql = f"""select * from project.{table}
              where {column} like '%{year}-{month}-{day}%'"""
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['0'], axis= 1)
    a = a.drop(['index'], axis= 1)      

    return eda(a)
 
def interpark_year( year,  eda ,col):

    con = connet()
    cursor = con.cursor()
    # project.  ---- db 이름
    sql  =  f"""select * FROM project.interpark_year_grade x
                left outer join project.interpark_year_info y 
                on x.`date` = y.`date` 
                left outer join project.interpark_year_sales z 
                on x.`date` = z.`date` 
                and z.`date` = '{year}'                
                where x.21 = y.187 
                and y.187 = z.319;
                """
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['0'], axis= 1)
    a = a.drop(['index'], axis= 1)
    a = a.drop(['date'], axis = 1)
    a['date'] = str(year)  
    
    return eda(a)

def interpark_month( year, month ,eda ,col):

    con = connet()
    cursor = con.cursor()
    # if :
    # project.  ---- db 이름
    sql  =  f"""select * FROM project.interpark_month_grade x
                left outer join project.interpark_month_info y 
                on x.`date` = y.`date` 
                left outer join project.interpark_month_sales z 
                on x.`date` = z.`date` 
                and z.`date` = '{year}{month}'
                where x.21 = y.188 
                and y.188 = z.319;
                """
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['0'], axis= 1)
    a = a.drop(['index'], axis= 1)
    a = a.drop(['date'], axis = 1)
    a['date'] = str(year)  
    print(eda(a))
    return eda(a)

def db_df_month(table ,column, year, month, eda ,col):

    con = connet()
    cursor = con.cursor()
    # project.  ---- db 이름
    sql = f"""select * from project.{table}
              where {column} like '%{year}{month}%'"""
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['0'], axis= 1)
    a = a.drop(['index'], axis= 1)      

    return eda(a)

def db_df_year(table ,column, year,eda ,col):

    con = connet()
    cursor = con.cursor()
    # project.  ---- db 이름
    sql = f"""select * from project.{table}
              where {column} like '%{year}%'"""
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    a = pd.DataFrame(result, columns = [col])
    a = a.drop(['0'], axis= 1)
    a = a.drop(['index'], axis= 1)      

    return eda(a)




##### columns name 
# yes24 eda - b_rank context review auther r_date publisher buplication - 7개
# kb eda columns - 단위 기간 카테고리 순위 제목 저자 출판사 출판연도 평점 리뷰개수 10개
# inter_y - rewview accuCnt aggrCnt author category title ProdNo rank 구매력? date 10개
# inter_m - rewview accuCnt aggrCnt author category title ProdNo rank 구매력? date 10개
# aladin - rank, title, author, publisher, pubDate, description, isbn10 price salesPoint wperiod




if __name__ == "__main__":
    # df = dropNull(khan_new(khan))
    # df_sep(df, 'khan_news')

    df = dropNull()


    # print(db_df_day('yes24_year','r_date','2022','10','',yes_def, yes_year).columns()) # yes24 clear
    # print(db_df_day('kb_monthly','기간','2022','1','',kyobo_dup, kb_month)) # kb clear
    # print(interpark_year( '2021', ip_year_total, interpark_y_t)) # inter park clear
    # print(interpark_month('2021','05',ip_month_total, interpark_m_t).columns) # inter park clear
    # print(aladin())   