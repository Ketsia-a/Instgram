from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import homepage, profile,user_profile,follow,unfollow,comment,search_users,likeView

urlpatterns = [

    path('', homepage , name ='homepage'),
    path('profile/<username>/', profile, name='profile'),
    path('user_profile/<username>/',user_profile,name='user_profile'),
    path('follow/<pk>', follow, name='follow'),
    path('unfollow/<pk>',unfollow, name='unfollow'),
    path('post/<pk>', comment, name='comment'),
    path('search/',search_users, name = 'searchs'),
    path('like/<int:pk>',likeView,name='like_post'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)