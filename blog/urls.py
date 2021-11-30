from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<slug:slug>/', views.blog_post, name='blog_post'),
    path('add_blog_post/', views.add_blog_post, name="add_blog_post"),
]
