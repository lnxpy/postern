from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'post/index.html', {})


def post(request, pk):
    return HttpResponse('You are looking for %s' % pk)
