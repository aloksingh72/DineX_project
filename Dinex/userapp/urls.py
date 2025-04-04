from django.urls import path
from .views import *


urlpatterns=[
  path("home/",user_home,name ="user_home"),
  path("user-cart/",user_cart,name="user_cart"),
  path('user-profile/',user_profile,name="user_profile"),
  path('add-to-cart/<int:product_id>/',add_to_cart,name="add_to_cart"),
  path('delete-from-cart/<int:cart_item_id>/',delete_from_cart,name="delete_from_cart"),
 

]

