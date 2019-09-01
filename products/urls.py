from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('error', views.error),
    path('getcard', views.getcard),
    path('getcard0', views.getcard0),
    path('getcard1', views.getcard1),
    path('getcard2', views.getcard2),
    path('getcard3', views.getcard3),
    path('getcard4', views.getcard4)

]