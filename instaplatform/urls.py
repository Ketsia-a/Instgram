from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import homepage, user_profile

urlpatterns = [

    path('', homepage , name ='homepage'),
    path('user_profile/<username>/', user_profile, name='user_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)