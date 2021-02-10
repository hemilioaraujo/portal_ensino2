from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base/home.html')


@login_required
def exibir_profile(request):
    return render(request, 'user/profile_usuario.html', {'user': request.user})


def xpto(request):
    ...
