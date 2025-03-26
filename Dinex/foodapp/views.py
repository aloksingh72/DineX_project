from django.shortcuts import render,redirect
from django.contrib import messages
from .models import AdminDetails
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

def categories_list(request):
    return render(request,"category/index.html")

def create_categories(request):
   if request.method == "POST":
        category_name = request.POST.get("category_name")
        print(category_name)
        admin_instance = Category()
        admin_instance.category_name = category_name
        admin_instance.save()



    return render(request,"category/createcategories.html")

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




def user_login(request):
    return render(request,"user_login.html")