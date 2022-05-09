from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home , name='home'),
    path('tasks', views.tasks , name='tasks'),
    path('delete',views.delete,name="delete"),
    path('update',views.update,name="update"),
    path('dataupdate',views.dataupdate,name="dataupdate"),
]
