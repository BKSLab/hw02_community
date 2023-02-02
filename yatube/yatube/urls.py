from django.contrib import admin
from django.urls import include, path

from posts.apps import PostsConfig

urlpatterns = [
    path('', include('posts.urls', PostsConfig.name)),
    path('admin/', admin.site.urls),
]
