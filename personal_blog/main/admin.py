from django.contrib import admin
from .models import Profile, PostDB

# Register your models here.


class ProfileView(admin.ModelAdmin):
    list_display = ('user', 'userId', 'bio', 'profession',
                    'workplace', 'gender', 'relationStatus', 'area', 'profilePic')


class PostDBView(admin.ModelAdmin):
    list_display = ('user', 'userId', 'post', 'created', 'updated')


admin.site.register(Profile, ProfileView)
admin.site.register(PostDB, PostDBView)
