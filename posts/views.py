from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def index(request):

    return HttpResponse('<h1>Welcome to django.</h1>')


def home(request):
    return HttpResponse('<h3>Welcome to my blog... .</h3>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)
