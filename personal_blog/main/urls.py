from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin_page, name='signin'),
    path('signup/', views.signup_page, name='signup'),
    path('complete_profile/', views.complete_profile, name='complete_profile'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home, name='home'),
]
