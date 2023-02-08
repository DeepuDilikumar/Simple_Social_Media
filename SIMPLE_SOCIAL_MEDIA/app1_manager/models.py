from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    title   = models.CharField(max_length = 100)
    image   = models.ImageField(upload_to = 'post_images', null = True)
    description = models.CharField(max_length = 500)
    date    = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    

