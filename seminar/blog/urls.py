from django.urls import path
from .views import AutorPosts, PostDetail, create_autor, create_post

urlpatterns = [
    path('post/<int:pk>', AutorPosts.as_view(), name='autor_post'),
    path('post/detail/<int:pk>', PostDetail.as_view(), name='detail_post'),
    path('autor/', create_autor, name='create_autor'),
    path('post/', create_post, name='create_post'),
]
