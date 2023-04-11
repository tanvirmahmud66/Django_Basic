from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # id ------------this id is unique for Profile db
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=150, blank=True, null=True)
    workplace = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, blank=True, null=True)
    relationStatus = models.CharField(max_length=150, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class PostDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PostDB"
        verbose_name_plural = "user's Post"
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.user.username
