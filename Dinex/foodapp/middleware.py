from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
#loggout middleware
class LogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Bypass for static/media files
        if request.path.startswith("/static/") or request.path.startswith("/media/"):
            return None  
        

        public_paths = [

            "/",
            "/admin_login/",
            "/admin_signup/",
            "/user_login/",
            "/user_signup/",
        ]

        # Exclude the admin login page to prevent infinite loop
        if request.path in public_paths:
            return None

        # Redirect only if user is not authenticated and trying to access protected pages
        if not request.user.is_authenticated:
            return redirect("/")  # Redirect to login page

        return None  # Continue processing other requests
