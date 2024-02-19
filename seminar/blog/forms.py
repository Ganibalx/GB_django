from django import forms
from .models import Post, Autor, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ['fullname']
        labels = {'firstname': 'Имя',
                  'lastname': 'Фамилия',
                  'bio': 'Биография',
                  'birthday': 'День рождения',
                  }


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()
    autor = forms.ModelChoiceField(queryset=Autor.objects.all())
    category = forms.CharField()
    views_count = forms.IntegerField(initial=0)
    publicate = forms.BooleanField(required=False)


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Autor.objects.all())
    content = forms.CharField(widget=forms.Textarea)
