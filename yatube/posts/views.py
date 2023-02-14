from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from posts.models import Group, Post
from posts.forms import PostForm
from yatube.settings import NOMBER_DISPLAYED_OBJECTS

User = get_user_model()


def index(request: object) -> Post:
    posts = Post.objects.all()
    paginator = Paginator(posts, NOMBER_DISPLAYED_OBJECTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'posts/index.html',
        {
            'posts': posts,
            'page_obj': page_obj,
        },
    )


def group_posts(request: object, slug: str) -> Group:
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, NOMBER_DISPLAYED_OBJECTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'posts/group_list.html',
        {
            'group': group,
            'posts': posts,
            'page_obj': page_obj,
        },
    )


def profile(request, username):
    user_name = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_name).all()
    count_posts = posts.count()
    paginator = Paginator(posts, NOMBER_DISPLAYED_OBJECTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
        'user_name': user_name,
        'count_posts': count_posts,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    count_posts = Post.objects.filter(author=post.author).count()
    context = {
        'post_id': post_id,
        'post': post,
        'count_posts': count_posts,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('posts:profile', request.user)

        return render(request, 'posts/create_post.html', {'form': form})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    is_edit = True
    post = get_object_or_404(Post, id=post_id)
    if request.method == "GET":
        if request.user != post.author:
            return redirect('post_detail', post_id=post.id)
        form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:profile', request.user)
    context = {
        'is_edit': is_edit,
        'post': post,
        'form': form,
        'post_id': post_id,
    }
    return render(request, 'posts/create_post.html', context)
