from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Autor, Post, Comment


class AutorPosts(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = Autor.objects.filter(pk=kwargs['pk']).first().firstname
        context['posts'] = Post.objects.filter(autor__id=kwargs['pk'])
        return context


class PostDetail(DetailView):
    template_name = 'blog/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=context['object']).order_by('create_date')
        context['comments'] = comments
        return context
