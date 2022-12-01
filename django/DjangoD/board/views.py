from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import pandas as pd
import numpy as np
import re
import datetime
import pymysql
from sqlalchemy import create_engine
def index(request):
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)

def db_to_df(table):
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='0000',
                        db='project2',
                        charset='utf8')

    engine = create_engine('mysql+pymysql://root:0000@localhost/project2')
    conn =engine.connect()
    data = pd.read_sql_table(table,conn)
    con.commit()
    con.close()
    return data

def main_view(request):
    data = db_to_df('context')

    context ={'df' : data}

    return render(request, 'templates/board/data.html', context)
