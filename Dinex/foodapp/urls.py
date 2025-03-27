from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name = "home"),
    path('admin-login/',admin_login,name="admin_login"),
    path('admin-signup/',admin_signup,name="admin_signup"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path('user-login/',user_login,name = "user_login"),
    # userdsignup path---->
    path('categories/',categories_list,name = "categories"),
    path('create-categories/',create_categories,name="create_categories"),

    #path for the edit categories
    path('edit-categories/<int:pk>/',edit_category,name="edit_category"),
    path('delete-category/<int:pk>/',delete_category,name="delete_category"),
]