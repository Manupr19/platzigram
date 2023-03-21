
from django.shortcuts import redirect

class ProfileCompletionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                return redirect('update_profile')
        response = self.get_response(request)
        return response