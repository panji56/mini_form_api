from django.shortcuts import render, redirect
from polls.models import forumPost
from django.contrib.auth.models import User
from polls.models import forumComment
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#Read list of posts here
def index(request):
    context = {}
    postList = forumPost.objects.all()
    context['postList'] = postList
    return render(request,'polls/index.html',context)

#view and controllers for user endpoints

#render view login page
def login(request):
    return render(request,'polls/login.html')

#render register login page
def register(request):
    return render(request,'polls/register.html')

#login mechanism
def loginSys(request):
    user = request.POST['user']
    pswd = request.POST['pass']
    #check if username exist
    user = authenticate(request,username=user,password=pswd)
    if user is not None:
        auth_login(request,user)
        # try:
        #     userObject = userForm.objects.get(username=user)
        #     #check if password match
        #     if userObject.values('password') == pswd:
        #         #set cookies with value (role,username)
        #         respon = HttpResponse(render('polls/index.html'))
        #         respon.set_cookie('username',userObject.values('username'),httponly=True)
        #         respon.set_cookie('role',userObject.values('username'),httponly=True)
        #         return respon
        #     else:
        #         print('password not match')
        #         return render(request,'polls/login.html')
        # except userForm.DoesNotExist:
        #     print('username does not exists')
        #     return render(request,'polls/login.html')
        return redirect('/forum')
    else:
        return HttpResponse(401)
    # return render(request,'polls/index.html')
#logout mechanism
def logout_web(request):
    logout(request)
    return redirect('/forum')

#create user
def createuser(request):
    user = request.POST['username']
    pwd = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(user,email,pwd)
    user.save()
    #also authencitated it at the same time
    user_auth = authenticate(request,username=user,password=pwd)
    auth_login(request,user_auth)
    #back to forum
    return redirect('/forum')

#view and controllers for post endpoints

#Read per post
def post(request):
    idp=request.GET['id_post']
    # checkCookies = request.COOKIES.get('username','None')
    # user = request.user.get_username()
    post = forumPost.objects.get(id_post = idp)
    comment = forumComment.objects.filter(id_post=idp)
    context = {}
    context['post'] = post
    context['comments'] = comment
    # context['checkCookies'] = checkCookies
    return render(request,'polls/post.html',context)

#Create post
@login_required
def CreatePost(request):
    #get the data
    if request.method=='POST':
        #insert it to post data model (ODM)
        # user=request.COOKIES.get('username')
        user = request.user
        postTittle=request.POST['postTittle']
        postContent=request.POST['postContent']
        post = forumPost(username=user,postTittle=postTittle,postText=postContent)
        post.save()
    return redirect('/forum')

#Update post
@login_required
def EditPost(request):
    if request.method=='POST':
        #update the post content per username
        # user=request.COOKIES.get('username')
        user = request.user
        post_id=request.POST['id_post']
        tittle=request.POST['postTittle']
        content=request.POST['postContent']
        # update content and tittle here
        # for admin need to search for the post id only because admin can update or delete all post, include comments
        post = forumPost.objects.filter(username=user).get(id_post=post_id)
        post.postTittle = tittle
        post.postText = content
        post.save()
    return redirect('/forum/viewpost?id_post='+post_id)

#Delete post
@login_required
def DeletePost(request):
    if request.method=='POST':
        # user=request.COOKIES.get('username')
        user = request.user
        post_id=request.POST['id_post']
        f_post = forumPost.objects.get(id_post=post_id)
        post = forumPost.objects.filter(username=user).get(id_post=f_post.id_post)
        #delete content here
        post.delete()
    return redirect('/forum')

#CRUD comment endpoints
#Delete Comment
@login_required
def DeleteComment(request):
    if request.method=='POST':
        # user=request.COOKIES.get('username')
        user=request.user
        post_id=request.POST['id_post']
        com_id=request.POST['id_comment']
        cm = forumComment.objects.filter(username=user).get(id_comment=com_id)
        cm.delete()
    return redirect('/forum/viewpost?id_post='+post_id)

#Update Comment
@login_required
def UpdateComment(request):
    if request.method=='POST':
        # user=request.COOKIES.get('username')
        user=request.user
        com_id=request.POST['id_comment']
        comment=request.POST['comment']
        id_post=request.POST['id_post']
        f_post = forumPost.objects.get(id_post=id_post)
        cm = forumComment.objects.filter(username=user).get(id_post=f_post)
        cm.comment = comment
        cm.save()
    return redirect('/forum/viewpost?id_post='+id_post)

#Create Comment
@login_required
def CreateComment(request):
    if request.method=='POST':
        # user=request.COOKIES.get('username')
        user=request.user
        comment=request.POST['comment']
        id_post=request.POST['id_post']
        f_post = forumPost.objects.get(id_post=id_post)
        cm = forumComment(username=user,id_post=f_post,comment=comment)
        cm.save()
    return redirect('/forum/viewpost?id_post='+id_post)
