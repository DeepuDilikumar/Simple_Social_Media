from django.urls import path

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static

from . import views

def sample(request):
    return render(request, 'new_post.html')

urlpatterns = [
    path('',views.user_login, name = 'login' ),
    path('home/', views.home, name = 'home'),
    path('create_account/', views.create_account, name = 'create_account'),
    path('create_new_post/', views.new_post, name = 'new_post'),
    path('logout/', views.user_logout, name = 'logout')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)