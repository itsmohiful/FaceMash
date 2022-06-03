from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=100,blank=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profile_picture/default_profile.jpg', upload_to='profile_picture')
    cover_photo = models.ImageField(default='cover_photo/default_cover.jpg', upload_to='cover_photo')
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
