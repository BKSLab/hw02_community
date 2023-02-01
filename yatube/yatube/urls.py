from django.contrib import admin
from posts.apps import PostsConfig
from django.urls import include, path

app_name = PostsConfig.name

urlpatterns = [
    path('', include('posts.urls', namespace=app_name)),
    path('admin/', admin.site.urls),
]
