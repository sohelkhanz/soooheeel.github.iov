from django.urls import path #importing the necessary documents

from . import views

app_name ='myapp'
urlpatterns = [
 path('', views.index, name='index'),
]