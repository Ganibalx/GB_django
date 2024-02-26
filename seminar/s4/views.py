from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .form import UserForm


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'C':
                return HttpResponseRedirect(f'../s3/coin/{count}')
            elif game == 'D':
                return HttpResponseRedirect(f'../s3/dice/{count}')
            elif game == 'R':
                return HttpResponseRedirect(f'../s3/random/{count}')
    else:
        form = UserForm()
    return render(request, 's4/index.html', {'form': form})



