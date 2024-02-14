from django.urls import path
from .views import AutorPosts, PostDetail

urlpatterns = [
    path('post/<int:pk>', AutorPosts.as_view(), name='autor_post'),
    path('post/detail/<int:pk>', PostDetail.as_view(), name='detail_post')
]
