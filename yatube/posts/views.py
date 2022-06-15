from django.shortcuts import render, get_object_or_404

from .models import Post, Group

LIM_POST: int = 10


def index(request):
    posts = Post.objects.select_related('group', 'author')\
        .order_by('-pub_date')[:LIM_POST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    description = 'Группа тайных поклонников графа'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:LIM_POST]
    context = {
        'group': group,
        'posts': posts,
        'description': description,
    }
    return render(request, 'posts/group_list.html', context)
