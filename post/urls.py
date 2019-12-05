from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:title>/', views.post, name='post')
]
