from cgitb import text
from turtle import title
from django.shortcuts import render, get_object_or_404

from .models import Post, Group

COUNT_STR: int = 10


def index(request):
    posts = Post.objects.select_related().order_by('-pub_date')[:COUNT_STR]
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'text': text,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи групп'
    text = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:COUNT_STR]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
