from django.shortcuts import get_object_or_404, render
from posts.models import Group, Post

NUMBER_POSTS = 10


def index(request):
    title = 'Это главная страница проекта Yatube!'
    posts = Post.objects.order_by('-pub_date')[:NUMBER_POSTS]

    return render(
        request,
        'posts/index.html',
        {
            'title': title,
            'posts': posts,
        },
    )


def group_posts(request, slug):
    title = (f'Записи сообщества {slug}')
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUMBER_POSTS]

    return render(
        request,
        'posts/group_list.html',
        {
            'title': title,
            'group': group,
            'posts': posts,
        },
    )
