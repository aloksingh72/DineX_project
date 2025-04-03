from django.shortcuts import render
from foodapp.models import *

# Create your views here.


# user home-page view
def user_home(request):
    category_instance = Category.objects.all()
    subcategory_instance = SubCategory.objects.all()
    
    return render(request,"userhome.html",context={"category_data":category_instance,"subcategory_data":subcategory_instance})



# cart view
def user_cart(request):


    return render(request,"navbar/usercart.html")

def user_profile(request):
    return render(request,"navbar/userprofile.html")