from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile, PostDB
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timesince import timesince
# Create your views here.


# @login_required(login_url='signin')
def signin_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Username or Password!!!")
            return redirect('signin')
    return render(request, 'signin_page.html')


# @login_required(login_url='signin')
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["confirm-password"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already used")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model,
                    userId=user_model.id
                )
                new_profile.save()
                user_auth = authenticate(username=username, password=password)
                if user_auth is not None:
                    login(request, user_auth)
                    return redirect('complete_profile')
                else:
                    return redirect('signup')
        else:
            messages.info(request, "Password not matched")
    return render(request, 'signup_page.html')


def complete_profile(request):
    if request.method == "POST":
        workplace = request.POST["workplace"]
        profession = request.POST["profession"]
        gender = request.POST["gender"]
        relationship = request.POST["relationship"]
        bio = request.POST["bio"]
        area = request.POST["district"]
        user = User.objects.get(id=request.user.id)
        if not user.is_staff:
            profile = Profile.objects.get(user=request.user)
            profile.workplace = workplace
            profile.profession = profession
            profile.gender = gender
            profile.relationStatus = relationship
            profile.bio = bio
            profile.area = area
            profile.save()
            return redirect('home')
    return render(request, 'complete_profile.html')


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def home(request):
    if request.method == "POST":
        user_model = User.objects.get(username=request.user)
        post = request.POST['postInput']
        new_post = PostDB.objects.create(
            user=user_model, userId=user_model.id, post=post
        )
        new_post.save()
        return redirect('home')
    posts = PostDB.objects.all()
    return render(request, 'home.html', {
        "posts": posts,
    })


@login_required(login_url='signin')
def profile_page(request, pk):
    user = User.objects.get(username=pk)
    user_post = PostDB.objects.filter(user=user)

    return render(request, 'profile_page.html', {
        "posts": user_post,
    })
