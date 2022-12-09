from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('question/', views.question, name='question'),
    path('resultBC', views.resultBC, name='resultBC'),
    path('resultBT', views.resultBT, name='resultBT'),
    path('resultIN', views.resultIN, name='resultIN'),
    path('resultLT', views.resultLT, name='resultLT'),
    path('resultLD', views.resultLD, name='resultLD'),
    path('resultLI', views.resultLI, name='resultLI'),
    path('resultLSA', views.resultLSA, name='resultLSA'),
    path('resultPR', views.resultPR, name='resultPR'),
    path('resultRP', views.resultRP, name='resultRP'),
]