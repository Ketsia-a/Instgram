from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login/')
def homepage(request):
    current_user = request.user
    userprofile= Profile.objects.filter(id = current_user.id).first()
    usercomments = Comments.objects.filter(id = current_user.id).first()

    return render(request, 'homepage.html', { "userprofile": userprofile, "usercomments": usercomments})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile_pictures = Posts.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()

    return render(request, 'profile.html', {"profi_images":profile_pictures, "my_profile":my_profile})

def likes(request,id):
   likes=0
   image = Image.objects.get(id=id)
   image.likes = image.likes+1
   image.save()
   
   return redirect("/")
