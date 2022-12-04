from django.shortcuts import render
from .models import BookTable,Buyc, LibInfo, LibPub
# Create your views here.

#하고 나서 해당 view와 urls 메인과 연결할 것
#def view_board()
from django.http import HttpResponse
from django.db import connection

def boardmodel(request):
    BuycList = Buyc.objects.filter(price= 99000)
    # context = {'BuycList': BuycList}
    # try:
    #     cursor = connection.cursor()
    #     strSql = "SELECT * FROM date"
    #     result = cursor.execute(strSql)
    #     datelist = cursor.fetchall()
    #     connection.commit()
    #     connection.close()
    # except:
    #     connection.rollback()
    #     print("Failed selecting in BookListView")
    
    # try:
    #     cursor = connection.cursor()
    #     strSql = "SELECT index,portal,price,sales FROM buyc WHERE price=99000"
    #     result = cursor.execute(strSql)
    #     BuycList = cursor.fetchall()
    #     connection.commit()
    #     connection.close()
    # except:
    #     connection.rollback()
    #     print("Failed selecting in BookListView")
    
    context ={'BuycList':BuycList}
    return render(request, 'board/boardlist.html',context)