from django.shortcuts import get_object_or_404, render

from posts.models import Group, Post
from yatube.settings import NOMBER_DISPLAYED_OBJECTS


def index(request: object) -> Post:
    posts = Post.objects.all()[:NOMBER_DISPLAYED_OBJECTS]

    return render(
        request,
        'posts/index.html',
        {
            'posts': posts,
        },
    )


def group_posts(request: object, slug: str) -> Group:
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NOMBER_DISPLAYED_OBJECTS]

    return render(
        request,
        'posts/group_list.html',
        {
            'group': group,
            'posts': posts,
        },
    )
