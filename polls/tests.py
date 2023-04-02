from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class test_mini_form_api(TestCase):
# testing the user end point

    #test the register user
    def test_Register(self):
        c = Client(enforce_csrf_checks=False)
        response = c.post('/forum/adduser',{'username':'mypanji','password':'121355Iu','email':'panji@mail.com'})
        print("Register Part")
        print(response.status_code)
        print(response.items())
        # the response is the location to '/forum'
        return response.content
    
    # test the user login
    def test_login(self):
        c = Client(enforce_csrf_checks=False)
        response = c.post('/forum/loginsys',{'user':'mypanji','pass':'121355Iu'})
        print("Login Part")
        print(response.status_code)
        return response.status_code
    
    #test to create the post per username
    def test_Insert_Post(self):
        #login to mini_forum_api first
        # self.user = User.objects.create_user(username='panji')
        # self.user.set_password('panji12345')
        # self.user.save()
        c = Client(enforce_csrf_checks=False)
        c.login(username='mypanji',password='121355Iu')
        response = c.post('/forum/insertpost',{'postTittle':'my first post','postContent':'lorem ipsum random text'})
        print(response.items())
        #the expected response is location to /forum
        return response.status_code
    
    #test to view the post
    def test_View_Post(self):
        c = Client(enforce_csrf_checks=False)
        response = c.get('/forum/viewpost',data={'id_post':1})
        print(response.dict())
    