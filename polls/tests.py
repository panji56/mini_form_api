from django.test import TestCase, Client

# Create your tests here.
class mini_form_api(TestCase):
# testing the user end point

    #test the register user
    def Register_Test(self):
        c = Client(enforce_csrf_checks=False)
        response = c.post('/forum/adduser',{'username':'mypanji','password':'121355Iu','email':'panji@mail.com'})
        print(response.content)
        return response.content
    
    # test the user login
    def Login_Test(self):
        c = Client(enforce_csrf_checks=False)
        response = c.post('/forum/loginsys',{'user':'mypanji','pass':'121355Iu'})
        print(response.status_code)
        return response.status_code
    
    #test to create the post per username
    def Insert_Post_Test(self):
        c = Client(enforce_csrf_checks=False)
        #login to mini_forum_api first
        c.login(username='panji',password='panji12345')
        response = c.post('/forum/insertpost',{'postTittle':'my first post','postContent':'lorem ipsum random text'})
        print(response.status_code)
        return response
    