from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post,Profile,Comment
from django.http import HttpResponse,Http404
# Create your views here.

@login_required(login_url='/accounts/login/')
def homepage(request):
    current_user = request.user
    userprofile= Profile.objects.filter(id = current_user.id).first()
    usercomments = Comment.objects.filter(id = current_user.id).first()

    return render(request, 'homepage.html', { "userprofile": userprofile, "usercomments": usercomments})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()

            return redirect('myprofile')
    else:
        form = NewProfileForm()

    return render(request, 'edit.html', {"form": form})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile_pictures = Posts.objects.filter(user = current_user)
    my_profile = Profile.objects.filter(user = current_user).first()

    return render(request, 'profile.html', {"profile_pictures":profile_pictures, "my_profile":my_profile})

@login_required(login_url='/accounts/login/')
def search_users(request):
  if 'username' in request.GET and request.GET["username"]:
      search_term = request.GET.get("username")
      searched_users = Profile.search_by_profile(search_term)
      message = f"{search_term}"

      return render(request, "search.html",{"message":message,"users": searched_users})
      
  else:
      message = "You haven't searched for any term"
      return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    user_images = Profile.objects.filter(user = current_user).first()
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = user_images
            image.save()

        return redirect('homepage')

    else:
        form = NewImageForm()

    return render(request, 'upload.html', {"form": form})


@login_required(login_url='/accounts/login/')
def add_comment(request, post_id):
    current_user = request.user
    image_item = Post.objects.filter(id = post_id).first()
    profiless = Profile.objects.filter( user = current_user.id).first()
    if request.method == 'POST':
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = profiless
            comment.commented_image = image_item
            comment.save()
            return redirect('homepage')
    else:
        form = commentForm()

    return render(request, 'comment.html', {"form": form, "post_id": post_id})

def likes(request,id):
    likes=0
    image = Post.objects.get(id=id)
    image.likes = image.likes+1
    image.save()
   
    return redirect("/")


@login_required(login_url='/accounts/login/')
def users_profile(request, ima_id):
    current_user = User.objects.filter(id = ima_id).first()
    profily_images = Post.objects.filter(user = current_user)
    my_profily = Profile.objects.filter(user = current_user).first()
    
    return render(request, 'users.html', {"profily_images":profily_images, "my_profily":my_profily})


