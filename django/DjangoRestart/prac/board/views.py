from django.shortcuts import render
from .models import Context, Date, NewsTable
# Create your views here.

#하고 나서 해당 view와 urls 메인과 연결할 것
#def view_board()
from django.http import HttpResponse
from django.db import connection

def boardmodel(request):
    #contextList = Context.objects.all()
    #context = {'contextLIst': contextList}
    try:
        cursor = connection.cursor()
        strSql = "SELECT * FROM date"
        result = cursor.execute(strSql)
        datelist = cursor.fetchall()
        connection.commit()
        connection.close()
    except:
        connection.rollback()
        print("Failed selecting in BookListView")
    
    context ={'datelist':datelist}
    return render(request, 'board/board_list.html',context)