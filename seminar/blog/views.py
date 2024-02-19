from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from .models import Autor, Post, Comment
from .forms import AuthorForm, PostForm, CommentForm


class AutorPosts(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor'] = Autor.objects.filter(pk=kwargs['pk']).first().firstname
        context['posts'] = Post.objects.filter(autor__id=kwargs['pk'])
        return context


class PostDetail(FormMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=context['object']).order_by('create_date')
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(author=data['author'],
                                   post=self.object,
                                   content=data['content'])
            return redirect('detail_post', self.object.pk)
        else:
            return self.form_invalid(form)


def create_autor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_autor')
    else:
        form = AuthorForm()
    return render(request, 'blog/create_autor.html', {'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(title=data['title'],
                                content=data['content'],
                                pub_date=data['pub_date'],
                                autor=data['autor'],
                                category=data['category'],
                                views_count=data['views_count'])
            return redirect('create_post')
    else:
        form = PostForm()
    return render(request, 'blog/create_autor.html', {'form': form})
