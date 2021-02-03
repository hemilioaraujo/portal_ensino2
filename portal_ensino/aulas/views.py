from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from portal_ensino.comentarios.models import Comentarios


# Create your views here.
@login_required
def aula(request):
    comentarios = Comentarios.objects.filter(aula_referente=request.user.aula_atual.id).order_by('data')
    return render(request, 'aulas/aula.html', {'usuario': request.user, 'comentarios': comentarios})
