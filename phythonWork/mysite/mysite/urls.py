from django.contrib import admin
from django.urls import path

from excelbigdata import views

urlpatterns = [
    path('upload/',views.upload, name='upload'),
    path('board_write/',views.board_write, name='board_write'),
    path('board_insert/',views.board_insert, name='board_insert'),
    path('', views.home, name='home'),
    path('board',views.board, name='board'),
    path('admin/',admin.site.urls),
    #path('excelmodel/',views.simple_upload),
]
