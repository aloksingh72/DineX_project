from django.urls import path
from .views import *


urlpatterns=[
  path("home/",user_home,name ="user_home"),

]