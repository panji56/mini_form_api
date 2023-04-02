from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userForm(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    role = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

class forumPost(models.Model):
    id_post = models.AutoField(auto_created=True,primary_key=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    postTittle = models.CharField(max_length=50, null=True)
    postText = models.TextField()

class forumComment(models.Model):
    id_comment = models.AutoField(auto_created=True,primary_key=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    id_post = models.ForeignKey(forumPost,on_delete=models.CASCADE)
    comment = models.TextField()