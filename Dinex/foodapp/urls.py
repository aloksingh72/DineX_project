from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name = "home"),
    path('admin-login/',admin_login,name="admin_login"),
    path('admin-signup/',admin_signup,name="admin_signup"),
    path('user-login/',user_login,name = "user_login"),
    # userdsignup path---->
]