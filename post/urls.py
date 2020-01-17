from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('user/<str:user>', views.user, name='user'),
    path('date/<str:date>', views.date, name='date'),
    path('user/<str:user>/<str:title>/', views.post, name='post'),
    path('new/', views.new, name='new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
