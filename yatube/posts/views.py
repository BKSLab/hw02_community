from django.shortcuts import get_object_or_404, render
from posts.models import Group, Post
from yatube.settings import LAST_PUBLICATIONS


def index(request: object) -> object:
    posts = Post.objects.all()[:LAST_PUBLICATIONS]

    return render(
        request,
        'posts/index.html',
        {
            'posts': posts,
        },
    )


def group_posts(request: object, slug: str) -> object:
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LAST_PUBLICATIONS]

    return render(
        request,
        'posts/group_list.html',
        {
            'group': group,
            'posts': posts,
        },
    )
