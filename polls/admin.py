from django.contrib import admin
from .models import userForm
from .models import forumComment
from .models import forumPost

# Register your models here.
admin.site.register(userForm)
admin.site.register(forumComment)
admin.site.register(forumPost)