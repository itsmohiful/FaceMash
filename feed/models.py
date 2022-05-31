from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to ="feeds/", null=True, blank=True)
    post_author = models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, null = True, blank=True, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    def __str__(self):
        return self.body
