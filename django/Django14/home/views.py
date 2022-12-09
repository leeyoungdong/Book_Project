from django.shortcuts import render
from .models import BookTable, Buyc, Information,Period, Reputation, LibDate,LibInformation,LibSA,LibTable
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def question(request):
    if request.method == 'POST':
        temp = request.POST.get('search_schema')
        context = str(temp)
        selectDatabase= {'context': context}
    return render(request, 'home/question.html', selectDatabase)


    #BookTable, Buyc, Information,Period, Reputation, LibDate,LibInformation,LibSA,LibTable
def resultBC(request):
    buycs = Buyc.objects.all()

    if 'portal' in request.GET: 
        keyword = request.GET['portal']
        if keyword: 
            buycs = buycs.filter(portal=keyword)

    if 'price' in request.GET: 
        sales = request.GET['price']
        if sales: 
            buycs = buycs.filter(price=sales)
    if 'sales' in request.GET: 
        sales = request.GET['sales']
        if sales: 
            buycs = buycs.filter(sales=sales)
    context = {
        'buycs': buycs, 
    }
    return render(request, 'home/resultBC.html',context)

def resultIN(request):
    info = Information.objects.all()
    #incode처리
    if 'title' in request.GET: 
        title = request.GET['title']
        if title:
            entitle = title.decode('UTF-8') 
            info = info.filter(title=entitle)

    if 'isbn' in request.GET: 
        isbn10 = request.GET['isbn']
        if isbn10: 
            info = info.filter(isbn=isbn10)

    if 'publisher' in request.GET: 
        pub = request.GET['publisher']
        if pub:
            enpub = pub.decode('UTF-8')
            info = info.filter(publisher=enpub)
    context = {
        'information': info, 
    }
    return render(request, 'home/resultIN.html',context)

def resultBT(request):
    books = BookTable.objects.all()
    if 'title' in request.GET: 
        title = request.GET['title']
        if title: 
            entitle = title.decode('UTF-8')            
            books = books.filter(title=entitle)

    if 'date' in request.GET: 
        date = request.GET['date']
        if date:
            endate =date.decode('UTF-8') 
            books = books.filter(date=endate)
    if 'author' in request.GET: 
        author = request.GET['author']
        if author:
            enauthor =author.decode('UTF-8') 
            books = books.filter(author=enauthor)

    context = {
        'books': books, 
    }
    return render(request, 'home/resultBT.html')
def resultPR(request):
    periods = Period.objects.all()

    if 'year' in request.GET: 
        year = request.GET['year']
        if year: 
            periods = periods.filter(year=year)

    if 'month' in request.GET: 
        month = request.GET['month']
        if month: 
            periods = periods.filter(month=month)
    if 'week' in request.GET: 
        week = request.GET['week']
        if week: 
            periods = periods.filter(week=week)
    if 'day' in request.GET: 
        day = request.GET['day']
        if day: 
            periods = periods.filter(day=day)   
    if 'pubdate' in request.GET: 
        pubdate = request.GET['pubdate']
        if pubdate: 
            enpubdate = pubdate.decode('UTF-8')
            periods = periods.filter(pub_date=enpubdate)   

    context = {
        'periods': periods, 
    }
    return render(request, 'home/resultPR.html',context)
    
def resultRP(request):
    reputations = Reputation.objects.all()

    if 'portal' in request.GET: 
        portal = request.GET['portal']
        if portal:
            enportal = portal.decode('UTF-8') 
            reputations = reputations.filter(portal=enportal)

    if 'rank' in request.GET: 
        rank = request.GET['rank']
        if rank: 
            enrank = float(rank)
            reputations = reputations.filter(rank=enrank)
    context = {
        'reputations': reputations, 
    }
    return render(request, 'home/resultRP.html',context)

def resultLT(request):
    libtables = LibTable.objects.all()

    if 'author' in request.GET: 
        author = request.GET['author']
        if author:
            enauthor =author.decode('UTF-8') 
            libtables = libtables.filter(author=enauthor)

    if 'title' in request.GET: 
        title = request.GET['title']
        if title: 
            entitle = title.decode('UTF-8')            
            libtables = libtables.filter(title=entitle)

    if 'pub' in request.GET: 
        pub = request.GET['pub']
        if pub:
            enpub = pub.decode('UTF-8')
 
            libtables = libtables.filter(pub=enpub)   
    context = {
        'libtables': libtables, 
    }
    return render(request, 'home/resultLT.html',context)


def resultLSA(request):
    libsas = LibSA.objects.all()

    if 'author' in request.GET: 
        author = request.GET['author']
        if author:
            enauthor = author.decode('UTF-8') 
            libsas = libsas.filter(author=enauthor)

    if 'price' in request.GET: 
        price = request.GET['price']
        if price: 
            libsas = libsas.filter(price=price)  

    context = {
        'libsas': libsas, 
    }
    return render(request, 'home/resultLSA.html',context)

def resultLI(request):
    libinfos = LibInformation.objects.all()

    if 'title' in request.GET: 
        title = request.GET['title']
        if title: 
            libinfos = libinfos.filter(title=title)

    if 'isbn' in request.GET: 
        isbn = request.GET['isbn']
        if isbn: 
            libinfos = libinfos.filter(isbn=isbn)  
    if 'isbnaddcode' in request.GET: 
        isbn_add_code = request.GET['isbnaddcode']
        if isbn_add_code: 
            libinfos = libinfos.filter(isbn_add_code=isbn_add_code)  
    context = {
        'libinfos': libinfos, 
    }
    return render(request, 'home/resultLI.html',context)

def resultLD(request):
    libdates = LibDate.objects.all()

    if 'pub' in request.GET: 
        pub = request.GET['pub']
        if pub:
            enpub = pub.decode('UTF-8') 
            libdates = libdates.filter(pub=enpub)

    if 'pubyear' in request.GET: 
        pubyear = request.GET['pubyear']
        if pubyear:
            dpubyear = float(pubyear)
            libdates = libdates.filter(pub_year=dpubyear)
    if 'pubmonth' in request.GET: 
        pubmonth = request.GET['pubmonth']
        if pubmonth:
            dpubmonth = float(pubmonth)
            libdates = libdates.filter(pub_month=dpubmonth)
    if 'pubday' in request.GET: 
        pubday = request.GET['pubday']
        if pubday:
            dpubday = float(pubday)
            libdates = libdates.filter(pub_day=dpubday)
    context = {
        'libdates': libdates, 
    }
    return render(request, 'home/resultLD.html',context)






