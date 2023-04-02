Mini Forum API

Mini Forum API is an simple API service that allows to make post per user, comment the post from another user. beside from creating the post or comment the user can edit the post or comment create by user.

To start the mini forum api open the root website:
http://localhost:8000/forum
OR replace localhost with the IP address of the server (the computer that run the django mini forum api)

after open the browser you will see the nav menu (HOME, LOGIN, LOGOUT, REGISTER) and the list of available posts to be read. you can read the post by click 'Show Post'. note that you need to login (or register) to make post or comment.

to begin with, start by follow step 1 but if you already register go to step 2 (perform login):
STEP 1: Register
1. Click 'Register' on the navigation menu.

![Main to Register](https://user-images.githubusercontent.com/42922801/229325210-3d286c5f-cc1d-4d63-9842-37d0bf44499a.JPG)

2. enter username and password (for username I recommended to use phone number or email because the usernames in the database has to be unique, if you can't create the username use phone or email)
3. enter email address
4. click Register
5. After success, you will be directed to main /forum page, where you can see the create post part
6. click one of the post list you can see that you can make comment to the post
