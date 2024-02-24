from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='core-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='core-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='core-post-delete'),
]