import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
from book_main_temp import *
from book_main import *

    # print(db_df_day('yes24_year','r_date','2022','10','',yes_def, yes_year).columns()) # yes24 clear
    # print(db_df_day('kb_monthly','기간','2022','1','',kyobo_dup, kb_month)) # kb clear
    # print(interpark_year( '2021', ip_year_total, interpark_y_t)) # inter park clear
    # print(interpark_month('2021','05',ip_month_total, interpark_m_t).columns) # inter park clear


if __name__ == "__main__":
    inter_m(interpark_month('2021','05',ip_month_total, interpark_m_t))
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