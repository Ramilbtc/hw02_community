from django.shortcuts import render, get_object_or_404

from .models import Post, Group

COUNT_POST: int = 10


def index(request):
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    a = 'group'
    b = 'author'
    posts = Post.objects.select_related(a, b).order_by('-pub_date')[:COUNT_POST]
    context = {
        'posts': posts,
        'text': text,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи групп'
    text = 'Лев Толстой - зеркало русской революции.'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:COUNT_POST]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
