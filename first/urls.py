"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import first,second_func,my_age
from posts.views import posts,get_tag_post, get_post
from django.utils.datastructures import MultiValueDictKeyError

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', first),
    path('second/', second_func),
    path('age/', my_age),
    path('get_posts/', posts),
    path('get_posts/<int:id>/', get_post, name="get_post"),
    path('get_posts/<str:title>/', get_tag_post, name="get_tag"),
    path('', include('books.urls')),
    path('users/', include('users.urls'))



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
