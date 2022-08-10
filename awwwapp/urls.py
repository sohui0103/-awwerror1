from django.contrib import admin
from django.urls import path
from awwwapp import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('musictalk/', views.musictalk, name = 'musictalk'),
    path('userplaylist/', views.userplaylist, name = 'userplaylist'),
    path('musicplaylist/', views.musicplaylist, name = 'musicplaylist'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('makeplaylist/', views.makeplaylist, name = 'makeplaylist'),
]