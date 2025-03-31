from django.shortcuts import redirect
from django.contrib.auth import logout

class LogoutMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if not request.user :
            logout(request)
            return redirect("/login/")
        return self.get_response(request)