from django.contrib import admin
from .models import Post

class Post_admin(admin.Model):
      list_display = (# nom colone BDD Poste) 
      



admin.site.register(Post)

# Register your models here.
