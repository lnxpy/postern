from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from . import models
from .forms import PostForm, Profile
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


# Create your views here.


def index(request):
    context = {
        'posts': list(reversed(models.Post.objects.all())),
        'is_admin': False,
    }
    print(context)
    user = User.objects.all()
    users = [i['username'] for i in user.values()]
    if str(request.user) in users:
        context['is_admin'] = True
    print(context['posts'])
    return render(request, 'post/index.html', context)


def post(request, user, title):
    context = {
        'post': get_object_or_404(models.Post.objects.filter(title=title, author=user))
    }
    return render(request, 'post/post.html', context)


def user(request, user):
    context = {
        'user': get_object_or_404(User.objects.filter(username=user)),
        'posts': reversed(models.Post.objects.filter(author=user)),
    }
    return render(request, 'post/user.html', context)


def date(request, date):
    context = {
        'posts': models.Post.objects.filter(publish=date),
        'date': date,
    }
    return render(request, 'post/date.html', context)


@login_required(login_url='/admin')
def new(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish = timezone.now()
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post/new.html', {'form': form})


@login_required(login_url='/admin')
def profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.publish = timezone.now()
            form.save()
            return redirect('home')
    else:
        form = Profile()
    return render(request, 'post/profile.html', {'form': form})
