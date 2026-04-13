from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='blog-home'),
    path('post/add/', views.create_post, name='post-create'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='post-edit'),
]