from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class LogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:  # Checks if user is logged in
            return None  # Allows the request to proceed

        # If user is not logged in, log out and redirect
        logout(request)
        return redirect("/admin_login/")  # Redirect to login page
