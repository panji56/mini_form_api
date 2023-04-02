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
4. click Login
![Register Fill Data](https://user-images.githubusercontent.com/42922801/229325333-4eef982b-b2f4-4891-a4db-f2ab719b2407.JPG)
6. After success, you will be directed to main /forum page, where you can see the create post part
![Main with Make a Post](https://user-images.githubusercontent.com/42922801/229325360-d6ee7e1e-f63c-487f-9245-3eeb165324b7.JPG)
8. click one of the post list. you can see that you can make comment to the post
![view post with make a comment](https://user-images.githubusercontent.com/42922801/229325455-69e74d9b-3817-4c29-aeb5-f51a44094e1d.JPG)
9. if you want to log out, click the LOGOUT link.

STEP 2: Login
1. After you logout or you already have an account in this API then click LOGIN
2. Enter the username (could be phone or email depends what you fill during username registration) and password
![Going to Login](https://user-images.githubusercontent.com/42922801/229325834-42092015-d5b2-4ceb-a64d-8e7c7117a20b.JPG)
3. Click login
4. if success, you will be redirected to main homepage '/forum', if not you will see 401 at the top left of the screen indicate that maybe the username does not exist or the password for the username does not match.
5. the view if user success login.
![Succesfull Login](https://user-images.githubusercontent.com/42922801/229325847-e37a386c-4151-44af-8aa3-13a8d11c1a06.JPG)

Now to the post feature, a user can create, edit, delete, and read post. only the owner of the post can edit, delete the post. any user (including not authenticated) can read all post. Let's create the first post.

Finally the comment feature. The comment feature use to give comment to the post. any user can give comment to any post belong to other user. However, the comment that you make can be seen by other user including both the owner of the post, authenticated user, guest user. the comment can be deleted or updated by the user who make the comment. Let's create the first comment.

ADMIN ROLE
