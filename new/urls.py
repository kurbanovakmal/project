from django.urls import path
from .views import BlogCreateViews,Blog,Blog2,BlogUpdateViews,BlogDeliteViews

urlpatterns = [
    path('post/<int:pk>/delite',BlogDeliteViews.as_view(),name='post_delite'),
    path('post/<int:pk>/edit',BlogUpdateViews.as_view(),name='post_edit'),
    path('post/new/',BlogCreateViews.as_view(),name='post_new'),
    path('',Blog.as_view(),name='home'),
    path('post/<int:pk>/',Blog2.as_view(),name='post')
]