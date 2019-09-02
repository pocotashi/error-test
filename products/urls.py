from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('error', views.error),
    path('getcard', views.getcard),
    path('<int:index>', views.productIndex)
]