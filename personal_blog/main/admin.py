from django.contrib import admin
from .models import Profile, PostDB, Verification

# Register your models here.


class ProfileView(admin.ModelAdmin):
    list_display = ('user', 'userId', 'bio', 'profession',
                    'workplace', 'gender', 'relationStatus', 'area', 'profilePic')


class PostDBView(admin.ModelAdmin):
    list_display = ('user', 'userId', 'post', 'created', 'updated')


class VerificationView(admin.ModelAdmin):
    list_display = ('user', 'token', 'is_verified')


admin.site.register(Profile, ProfileView)
admin.site.register(PostDB, PostDBView)
admin.site.register(Verification, VerificationView)
