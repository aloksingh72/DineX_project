from django.shortcuts import render,redirect
from foodapp.models import *
from django.db.models import Sum, F
# Create your views here.


# user home-page view
def user_home(request):
    category_instance = Category.objects.all()
    subcategory_instance = SubCategory.objects.all()
    product_instance = Product.objects.all()
    
    return render(request,"userhome.html",context={"category_data":category_instance,
                                                   "subcategory_data":subcategory_instance,
                                                   "product_data":product_instance})

# cart view
def user_cart(request):
    cart_items = Cart.objects.all()
    total_price = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total'] or 0

    return render(request,"navbar/usercart.html",context= {"cart_items":cart_items,"total_price":total_price})

def add_to_cart(request,product_id):
    product = Product.objects.filter(id = product_id).first()
    if product:
        cart_items, created = Cart.objects.get_or_create(product = product)

        if not created:
            cart_items.quantity +=1
            cart_items.save()
            
    return redirect("user_home")


def delete_from_cart(request,cart_item_id):
    cart_items = Cart.objects.filter(id = cart_item_id).first()
    if cart_items:
      cart_items.delete()
    return redirect("user_cart")

def buy_now(request,product_id):
    product = Product.objects.filter(id = product_id).first()
    if product:
        cart_items, created = Cart.objects.get_or_create(product = product)

        if not created:
            cart_items.quantity +=1
            cart_items.save()

    return redirect("user_cart")




def user_profile(request):
    return render(request,"navbar/userprofile.html")