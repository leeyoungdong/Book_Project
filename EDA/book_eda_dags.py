import pandas as pd
import numpy as np
import re
from datetime import timedelta
import datetime
import pymysql
from sqlalchemy import create_engine
from book_main_temp import *
from book_main import *

a = datetime.datetime.now()

def get_date(y, m, d):
  '''y: year(4 digits)
   m: month(2 digits)
   d: day(2 digits'''
  s = f'{y:04d}-{m:02d}-{d:02d}'
  return datetime.datetime.strptime(s, '%Y-%m-%d')

def get_week_no(y, m, d):
    target = get_date(y, m, d)
    firstday = target.replace(day=1)
    if firstday.weekday() == 6:
        origin = firstday
    elif firstday.weekday() < 3:
        origin = firstday - timedelta(days=firstday.weekday() + 1)
    else:
        origin = firstday + timedelta(days=6-firstday.weekday())
    return (target - origin).days // 7 + 1

week = get_week_no(int(a.strftime("%Y")),int(a.strftime("%m")),int(a.strftime("%d")))

if __name__ == "__main__":

    # inter_m(interpark_month('2021','05',ip_month_total, interpark_m_t))
    # inter_y(interpark_year('2021',ip_year_total, interpark_y_t))

    # kb_y(db_df_year('{}','기간',a.strftime("%Y"),kyobo_dup, kb_year)) # yes24 clear
    
    # kb_m(db_df_month('{}','기간',a.strftime("%Y"),a.strftime("%m"),kyobo_dup, kb_month))
    # yes_y(db_df_month('yes24_year_every','date',a.strftime("%Y"),a.strftime("%m"),yes_def, yes_year))

    ############################yes_d(db_df_day('yes24_day_daily','date',a.strftime("%Y"),a.strftime("%m"),a.strftime("%d"),yes_def,yes_day))
    
    # kb_w(db_df_week('{}','기간',a.strftime("%Y"),a.strftime("%m"),week,kyobo_dup, kb_week))
    #################### yes_m(db_df_week('yes24_week_weekly','date',a.strftime("%Y"),a.strftime("%m"),week,yes_def,yes_month))
    # aladin(ala_week('alading_week_every','wperiod',a.strftime("%Y"),a.strftime("%m"),week,aladina,'1'))
    # print(db_df_day('kb_monthly','기간','2022','1','',kyobo_dup, kb_month)) # kb clear
    # yes_d()
    # yes_m()   
    # yes_y()
    # kb_m()
    # kb_w()
    # kb_y()
    # inter_y()
    # aladin()
    # df = dropNull(khan_new(khan))
    # df_sep(df, 'khan_news')
    # print(db_df_day('yes24_year','r_date','2022','10','',yes_def, yes_year).columns()) # yes24 clear
    # print(db_df_day('kb_monthly','기간','2022','1','',kyobo_dup, kb_month)) # kb clear
    # print(interpark_year( '2021', ip_year_total, interpark_y_t)) # inter park clear
    # print(interpark_month('2021','05',ip_month_total, interpark_m_t).columns) # inter park clear