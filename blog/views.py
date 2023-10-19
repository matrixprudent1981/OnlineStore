from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from blog.models import Post


# Create your views here.

def helloView(request):
    return HttpResponse("<h1>Привет это магазин Lucky</h1>")


def now_date_view(request):
    return HttpResponse(f"Сегодня: {datetime.date.today()}")


def goodbyeView(request):
    return HttpResponse("<h1>Good bye user</h1>")


def postlistview(request):
    posts = Post.objects.all()
    html_name = 'post/posts.html'
    context = {
        "posts": posts,
    }
    return render(request, html_name, context)


def postDetailInfo(request, id):
    post = get_object_or_404(Post, id=id)
    html_name = 'post/post_detail.html'
    context = {
        'post': post
    }
    return render(request, html_name, context)
