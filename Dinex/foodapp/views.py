from .models import SubCategory
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,"home.html")


def admin_logout(request):
    logout(request)  # Logs out the user
    request.session.flush()  # Clears session data
    messages.success(request, "Logged out successfully!")
    return redirect("admin_login")  # Redirects to login page

def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        #    admin_instance = authenticate(request,email = email,password = password)
        admin_instance = UserDetails.objects.get(email= email)

        if admin_instance.role == "admin":
            if check_password(password,admin_instance.password):
                        login(request, admin_instance)
                        print("admin_login=============>")
                        request.session["admin_id"] = admin_instance.id
                        messages.success(request,"Admin login succesful")
                        return redirect("admin_dashboard")
            else:
                messages.error(request,"Not an  Admin account")
                return redirect("admin_login")
       
    return render(request,"admin_login.html")


# def admin_signup(request):
#     if request.method == "POST":
#      username = request.POST["username"]
#      email = request.POST["email"]
#      password = request.POST["password"]
#      confirm_password = request.POST["confirm_password"]

#      if  password != confirm_password:
#         messages.error(request,"Passwords does not match")
#         return redirect("admin_signup")
    
#      if UserDetails.objects.filter(email = email).exists():
#         messages.error(request,"Email is already exists")
#         return redirect("admin_signup")
    
#      if UserDetails.objects.filter(username = username).exists():
#       messages.error(request,"username is already exists")
#       return redirect("admin_signup")
#     #  hashing password 
#      hashed_password = make_password(password)

#      admin = UserDetails(username = username,email = email,password = hashed_password)
#      admin.save()
#      messages.success(request,"Admin registered successfully")
#      return redirect("admin_login")
    
#     return render(request,"admin_signup.html")

def admin_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('admin_signup')
        
        if UserDetails.objects.filter(username = username).exists():
            messages.error(request,"username is already exists")
            return redirect("admin_signup")

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('admin_signup')

        UserDetails.objects.create_user(
            username=username,
            email=email,
            password=password,
            confirm_password=confirm_password,
            role="admin"
        )
        messages.success(request, "Admin registered successfully.")
        return redirect('admin_login')

    return render(request, "userapp/admin_signup.html")


def admin_dashboard(request):
   
   category_count = Category.objects.count()
   sub_category_count = SubCategory.objects.count()
   product_count= Product.objects.count()

   return render(request,"index.html",context={"category_count":category_count,
                                               "sub_category_count":sub_category_count,
                                               "product_count":product_count})


def user_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        #  adding the validation
        if password != confirm_password:
            messages.error(request,"Passwords do not match")
            return redirect("user_signup")
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request,"Email is already registered")
            return redirect("user_signup")
        
        UserDetails.objects.create_user(
            username = username,
            email = email,
            password = password,
            confirm_password = confirm_password,
            role = "user"
        )
        messages.success(request,"User registered successfully")
        return redirect("user_login")
         
    return render(request,"user_signup.html")


def user_login(request):
    if request.method =="POST":
        email = request.POST["email"]
        password= request.POST["password"]

        user_instance = UserDetails.objects.get(email = email)
        if user_instance.role =="user":
            if check_password(password,user_instance.password):
                 login(request, user_instance)
                 print("user_login==========>")
                 request.session["user_id"] = user_instance.id
                 messages.success(request,"User login successful")
                 return redirect("/user/home/")
                    
    return render(request,"user_login.html")

def user_logout(request):
    logout(request)
    return redirect('home')


# view for show the listing of the category
def categories_list(request):
   query = request.GET.get('query','')
   if query:
    category = Category.objects.filter(category_name__icontains = query)
    category = category.order_by("id")
   else:
    category = Category.objects.all().order_by("id")

    # making object of the model
 
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
    query = request.GET.get('query','')
    print(query)
    if query:
        subcategories = SubCategory.objects.filter(category__category_name__icontains=query) | SubCategory.objects.filter(sub_category_name__icontains=query)
        subcategories = subcategories.order_by("-id")
        # subcategories = SubCategory.objects.filter(sub_category_name__icontains = query).order_by("id")
    else:
        subcategories = SubCategory.objects.all().order_by("-id")  # Fetch all subcategories

 
    return render(request, "subcategory/index.html", {"subcategories": subcategories})

#create_sub_categories
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

#edit sub_categories
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

# delete sub_categories
def delete_sub_categories(request,subcategory_id):
    sub_category_instance = SubCategory.objects.filter(id = subcategory_id).last()
    sub_category_instance.delete()
    return redirect("sub_category_list")
    
    


# --------------------------------views for products----------------------------------
def product_list(request):
    query = request.GET.get('query','')
    if query:
        product_instance = Product.objects.filter(prod_name__icontains = query).order_by("id")
    else:
         product_instance = Product.objects.all().order_by("-id")

    return render(request,"product/index.html",context={"product_data":product_instance})

# views for create_product 
# def create_product(request):
#     categories = Category.objects.all()
#     sub_categories = SubCategory.objects.none()


#     selected_categories_id = request.GET.get("category","")

#     if selected_categories_id:
#         sub_categories = SubCategory.objects.filter(category_id = selected_categories_id)

#     if request.method == "POST":
#         category_id = request.POST.get("category")
#         sub_category_id = request.POST.get("sub_category")
#         product_name = request.POST.get("product_name")
#         price = request.POST.get("price")
#         description = request.POST.get("description")

#         #geting categories and sub-categories instances
#         category = Category.objects.get(id = category_id)
#         sub_category = SubCategory.objects.get(id = sub_category_id)

#         # Create and Save the Product
#         Product.objects.create(
#             category = category,
#             sub_category = sub_category,
#             prod_name = product_name,
#             price = price,
#             description = description

#         )
#         return redirect("products")
    
#     return render(request,"product/createproduct.html",
#                   context={"categories":categories,
#                            "sub_categories":sub_categories,
#                            "selected_categories_id":selected_categories_id,})

#load categories
def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'sub_category_name')
    return JsonResponse(list(subcategories), safe=False)

# create product 
def create_product(request):
    
    categories = Category.objects.all()
    selected_category_id = request.GET.get("category", "")  # Get category ID from request
    sub_categories = SubCategory.objects.all()  # Default empty list

    # If a category is selected, filter subcategories
    if selected_category_id.isdigit():
        sub_categories = SubCategory.objects.filter(category_id=selected_category_id)

    if request.method == "POST":
        category_id = request.POST.get("category")
        sub_category_id = request.POST.get("sub_category")
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        product_image = request.FILES.get("product_image")  

        # Validate category selection
        if category_id and sub_category_id:
            category = Category.objects.get(id=category_id)
            sub_category = SubCategory.objects.get(id=sub_category_id)

            # Create and save the product
            Product.objects.create(
                category=category,
                sub_category=sub_category,
                prod_name=product_name,
                price=price,
                description=description,
                product_image=product_image,
            )
            return redirect("products")  # Redirect after successful save
  
    return render(request, "product/createproduct.html", {
        "categories": categories,
        "sub_categories": sub_categories,
        "selected_category_id": selected_category_id,
    })

def edit_product(request,product_id):
    product = Product.objects.get(id=product_id) 
    
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.filter(category = product.category)

    if request.method  =='POST':
        product.prod_name = request.POST.get("product_name")
        product.price = request.POST.get("product_price")
        product.description = request.POST.get("product_description")
        category_id = request.POST.get("category")
        sub_category_id = request.POST.get("sub_category")
       

        # Update category and subcategory if selected
        if category_id:
            try:
                product.category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                pass  # Ignore if invalid category is provided

        if sub_category_id:
            try:
                product.sub_category = SubCategory.objects.get(id=sub_category_id)
            except SubCategory.DoesNotExist:
                pass  

            product.save()
            return redirect("products")

    return render(request,"product/editproduct.html",
                  context={"product":product,"categories":categories,"sub_categories":sub_categories})

def delete_product(request,product_id):
    product_instance = Product.objects.filter(id=product_id).last()
    product_instance.delete()
    return redirect("products")

def get_data(request):
    if request.method == "GET":
        a = request.GET.get('category_id')
        sub_categories_list = SubCategory.objects.filter(category_id=a).all().values('id','sub_category_name')
        print(a)
      
        return JsonResponse(list(sub_categories_list), safe=False)
    


def show_analytics(request):
    return render(request,"analytics.html")

  