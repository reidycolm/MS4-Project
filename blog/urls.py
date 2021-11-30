from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<slug:slug>/', views.blog_post, name='blog_post'),
    path('add_blog_post/', views.add_blog_post, name="add_blog_post"),
    path('edit_blog_post/<int:post_id>/', views.edit_blog_post, name="edit_blog_post"),
    path('delete_blog_post/<int:post_id>/', views.delete_blog_post, name="delete_blog_post"),
]
