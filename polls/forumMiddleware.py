from django.http import HttpResponse
from polls.models import userForm

class forumMiddleware(object):
    
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response = self.get_response(request)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        #list for site open for guest
        openGuest = ['/forum/','/forum/login/','/forum/viewpost']
        #list for site open only to authencitated user
        AuthOnly = ['/forum/loginSys','/forum/insertpost']
        #check for url path match the guest site
        if request.path_info in openGuest:
            return None
        #check for url path match the site for authencitated user
        if request.path_info in AuthOnly:
            user=request.COOKIES.get('username','None')
            role=request.COOKIES.get('role','None')
            #check if user login and exist
            if((user == 'None') & (role == 'None')):
                return HttpResponse(401)
            else:
                try:
                    userForm.objects.get(username=user)
                except:
                    return HttpResponse(401)
                return None
