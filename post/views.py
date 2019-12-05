from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from . import models

# Create your views here.


def index(request):
    context = {
        'posts': reversed(models.Post.objects.all())
    }
    return render(request, 'post/index.html', context)


def post(request, title):
    context = {
        'post': get_object_or_404(models.Post.objects.filter(title=title))
    }
    print(context['post'])
    return render(request, 'post/post.html', context)
