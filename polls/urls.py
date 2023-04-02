from django.urls import include,path
# import django.contrib.auth
from . import views

urlpatterns = [
    #for views
    path('',views.index,name='index')
    ,path('login',views.login,name='login')
    ,path('logout',views.logout_web,name='logout')
    ,path('register',views.register,name='Register User')
    ,path('adduser',views.createuser,name='Register User')
    #for CRUD endpoints
    #for POST CRUD endpoints
    #read
    ,path('viewpost',views.post,name='post')
    #create
    ,path('insertpost',views.CreatePost,name='createpost')
    #update
    ,path('updatepost',views.EditPost,name='edit post')
    #delete
    ,path('deletepost',views.DeletePost,name='delete post')
    #for comment CRUD endpoints
    #update
    ,path('updatecomment',views.UpdateComment,name='update comment')
    #delete
    ,path('deletecomment',views.DeleteComment,name='delete comment')
    #create
    ,path('makecomment',views.CreateComment,name='make comment')

    #for login endpoints
    ,path('loginsys',views.loginSys,name='login system')
]