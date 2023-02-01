from posts.apps import PostsConfig
from django.urls import path
from posts.views import group_posts, index


app_name = PostsConfig.name

urlpatterns = [
    path('', index, name='h_page'),
    path('group/<slug:slug>/', group_posts, name='page_post'),
]
