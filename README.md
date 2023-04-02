Mini Forum API

Mini Forum API is an simple API service that allows to make post per user, comment the post from another user. beside from creating the post or comment the user can edit the post or comment create by user.

before you start to use the mini forum API you want to set it up first by click the link here:
[api_setup.md](https://github.com/panji56/mini_form_api/blob/39daba83e6b85a3d07106f09a7bf7cda93d2628a/api_setup.md)

the requirements is that python 3.7+, Django, django-bootstrap-v5, django-jquery must be installed

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
1. Enter the post tittle and the post content on the 'Make a Post' part
2. Click submit
![Make a Post](https://user-images.githubusercontent.com/42922801/229326747-1d63eb57-9c18-422c-b4d3-0c0995b8dc2f.JPG)
3. you will see the post you have just inserted by looking at the post list. the post ussually appear at the bottom of the list. after the post title there is a 'by' word and after that word is the username who created the post. Click 'Show Post' on the post based on your username if you want to edit or delete it.
![Show Post per User](https://user-images.githubusercontent.com/42922801/229326790-090193a3-2f40-482b-b407-fab110dd1fdd.JPG)
5. after click show now you can see that you can edit the post content and tittle also delete it.
![view post just created](https://user-images.githubusercontent.com/42922801/229326819-9e9de118-ed85-42fc-9eb6-a67209d825ac.JPG)

Update the Post
Update the post mean change the tittle or content or both. the text for tittle and content will be loaded to the input text to make it easier to edit the content or tittle. just change the text in tittle or content post then click 'Update'.
![Update Post User](https://user-images.githubusercontent.com/42922801/229326866-e082be9f-642d-4393-a8bd-268b1802d928.JPG)
here is the result
![Updated Post](https://user-images.githubusercontent.com/42922801/229326869-e1e07cb3-123b-4593-a7aa-39ea52808a26.JPG)

Delete the Post
to delete the post, just click the Delete Post Button. When you delete the post the comment related to the post will also be deleted. after that you will be redirected to main '/forum' page again.

Finally the comment feature. The comment feature use to give comment to the post. any user can give comment to any post belong to other user. However, the comment that you make can be seen by other user including both the owner of the post, authenticated user, guest user. the comment can be deleted or updated by the user who make the comment. Let's create the first comment.
1. Let's open other post created by different user. for example the post created by user 'panji'.
![PostList](https://user-images.githubusercontent.com/42922801/229327132-90dbc771-1951-46b7-a914-121a2016812e.JPG)
2. on the 'Give a comment the Post' part you can fill the text area in that part and click submit
![Make a Comment to Another user](https://user-images.githubusercontent.com/42922801/229327186-a0118645-ec97-4c7c-b6c6-da1386bc85e3.JPG)
4. the comment will be seen on the comments. you also see the update and delete comment part.
![Show comment for the post](https://user-images.githubusercontent.com/42922801/229327313-40d72fb1-dcd8-40b3-a6e0-7d5287cd15de.JPG)

Update the comment. After you can make the comment you can update the comment. but remember the text area to modify the comment is very small so you have to be very careful if you want to change it. to begin with change the text for the comment part on the right side and click 'Update Comment'.
![update the comment](https://user-images.githubusercontent.com/42922801/229327856-81066b11-a006-4358-860a-300ab590f44c.JPG)
Change the comment
![Updated Comment](https://user-images.githubusercontent.com/42922801/229327870-fb1322fd-3004-4f69-a599-68d86122383c.JPG)
Updated comment

Delete Comment. for delete comment just click the comment that created. once press Delete it will reload the view post page and the comment will be dissapear.

ADMIN ROLE
What is ADMIN Role OR ADMIN user. ADMIN user is a type of user that can bypass all the ownership. which mean the user can make, update, delete, read post belong to other user and also make, update, delete, comment. to indicate if user is an admin or not go to the main page '/forum' and look for the top left below the HOME, LOGIN, LOGOUT, REGISTER link. there is a table with username, role, is Admin. if the is Admin is True then the user has ADMIN Role.
![Forum API Admin User](https://user-images.githubusercontent.com/42922801/229329243-a9c98763-8460-4d99-ae8d-ceef2865983d.JPG)

the operation on post and comment are still the same with the difference is that on the viewpost you can edit the post and comment that is belong to other user.

Where I can create user with the admin role ?
unfortunately you can't create user within the '/forum' page (or path). this indicate that when you register you actually create a user without an admin role. the reason behind this is the security. on the real production server you don't want anyone to create admin user which cause your post and comment to be modified unresponsibly. hence, to create a user admin it has to be in a local network (or office network) where only a certain people can access the network. the site or path to create admin user is 'http://<your_host_ip_address>:8000/admin. this '/admin' path will be block if someone try to access from the internet. however, you can login on the '/forum' site as an admin user from the internet. on this mini forum api go to the file 'admin.txt' and find the user start with 'admin'. use the user 'admin' and it's password to login to the mini forum api as an admin user. the file also contain users for documentation and testing purpose only.
