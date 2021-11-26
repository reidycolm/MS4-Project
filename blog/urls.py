from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<slug:slug>/', views.blog_post, name='blog_post'),
]
