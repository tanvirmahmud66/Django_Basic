from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin_page, name='signin'),
    path('signup/', views.signup_page, name='signup'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home, name='home'),
    path('profile/<str:pk>/', views.profile_page, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete'),
    path('edit_post/<str:pk>/', views.edit_post, name="edit"),
    path('profile_pic/', views.edit_pp, name='editpp'),
]
