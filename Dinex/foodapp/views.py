from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.
def home(request):
    return render(request,"home.html")


def admin_logout(request):
    request.session.flush()  # Clear session
    messages.success(request, "Logged out successfully!")
    return redirect("admin_login")


def admin_login(request):
    if request.method == "POST":
       email = request.POST["email"]
       password = request.POST["password"]
       
    #    admin_instance = authenticate(request,email = email,password = password)
       admin_instance = AdminDetails.objects.get(email= email)
       if check_password(password,admin_instance.password):
                    print("user_login=============>")
                    request.session["admin_id"] = admin_instance.id
                    messages.success(request,"Admin login succesful")
                    return redirect("admin_dashboard")
       
    return render(request,"admin_login.html")

def admin_dashboard(request):
   return render(request,"index.html")


# view for show the listing of the category
def categories_list(request):
    # here we have to show the listing 
    # making object of the model
    category = Category.objects.all().order_by("id")
    return render(request,"category/index.html",context={"category_data":category})

def edit_category(request,pk):
    edit_cat = Category.objects.filter(id =pk).last()
    print(edit_cat,"<==================>")
    if request.method == "POST":
        new_category_name = request.POST.get("edit_category")
        if new_category_name:
            edit_cat.category_name = new_category_name
            edit_cat.save()
            return redirect("categories")

    return render(request,"category/editcategory.html",context={"edit_category":edit_cat})

def delete_category(request,pk):
    delete_category = Category.objects.filter(id= pk).last()
    delete_category.delete()
    return redirect("categories")


    # return render(request,"category/deletecategory.html")

def create_categories(request):
   if request.method == "POST":
        category_name = request.POST.get("category_name")
        print(category_name)
        admin_instance = Category()
        admin_instance.category_name = category_name
        admin_instance.save()
        return redirect("categories")

   return render(request,"category/createcategories.html")

def sub_category_list(request):
    subcategories = SubCategory.objects.all().order_by("id")  # Fetch all subcategories
    return render(request, "subcategory/index.html", {"subcategories": subcategories})


def create_sub_categories(request):
    create_sub_cat = Category.objects.all().order_by("id")
    if request.method == "POST":
        category_id = request.POST.get("category")
        sub_category_name = request.POST.get("sub_category_name")
        print(sub_category_name)
        if category_id and sub_category_name:
            category = Category.objects.get(id=category_id)  # Fetch category instance
            sub_category_instance = SubCategory.objects.create(category=category, sub_category_name=sub_category_name)  
            sub_category_instance.save()

            return redirect("sub_category_list") 
    return render(request,"subcategory/createsubcategory.html",context={"create_sub_cat":create_sub_cat})


def edit_sub_categories(request,subcategory_id):
      edit_subcategory = SubCategory.objects.get(id=subcategory_id)
      categories = Category.objects.all()
       
      if request.method == "POST":
        category_id = request.POST.get("category")  # Get selected category from dropdown
        sub_category_name = request.POST.get("sub_category_name")  # Get updated subcategory name

        if category_id and sub_category_name:
            edit_subcategory.category = Category.objects.get(id=category_id)  # Update category
            edit_subcategory.sub_category_name = sub_category_name  # Update subcategory name
            edit_subcategory.save()  # Save changes

            return redirect("sub_category_list")


      return render(request,"subcategory/editsubcategory.html",
                    context={"edit_subcategory":edit_subcategory,"categories":categories})

def delete_sub_categories(request,subcategory_id):
    sub_category_instance = SubCategory.objects.filter(id = subcategory_id).last()
    sub_category_instance.delete()
    return redirect("sub_category_list")
    
    

def admin_signup(request):
    if request.method == "POST":
     username = request.POST["username"]
     email = request.POST["email"]
     password = request.POST["password"]
     confirm_password = request.POST["confirm_password"]

     if  password != confirm_password:
        messages.error(request,"Passwords does not match")
        return redirect("admin_signup")
    
     if AdminDetails.objects.filter(email = email).exists():
        messages.error(request,"Email is already exists")
        return redirect("admin_signup")
    
     if AdminDetails.objects.filter(username = username).exists():
      messages.error(request,"username is already exists")
      return redirect("admin_signup")
    #  hashing password 
     hashed_password = make_password(password)

     admin = AdminDetails(username = username,email = email,password = hashed_password)
     admin.save()
     messages.success(request,"Admin registered successfully")
     return redirect("admin_login")
    
    return render(request,"admin_signup.html")

# --------------------------------views for products-------------------------
def product_list(request):
    return render(request,"product/index.html")

# views for create_product 
def create_product(request):
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    if request.method == "POST":
        category_id = request.POST.get("category")
        sub_category_id = request.POST.get("sub_category")
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        #geting categories and sub-categories instances
        category = Category.objects.get(id = category_id)
        sub_category = SubCategory.objects.get(id = sub_category_id)

        # Create and Save the Product
        Product.objects.create(
            category = category,
            sub_category = sub_category,
            prod_name = product_name,
            price = price,
            description = description


        )
        return redirect("products")
    


    return render(request,"product/createproduct.html",
                  context={"categories":categories,"sub_categories":sub_categories})

def user_login(request):

    return render(request,"user_login.html")