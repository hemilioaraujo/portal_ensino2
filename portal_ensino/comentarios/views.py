from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from portal_ensino.aulas.models import Aulas
from portal_ensino.base.models import User
from portal_ensino.comentarios.models import Comentarios

def post_comentario(request):
    resposta = request.POST
    comentario = resposta['comentario']
    usuario = User.objects.get(id=request.user.id)
    aula_referente = Aulas.objects.get(id=request.user.aula_atual.id)

    try:
        Comentarios.objects.create(
            comentario=comentario,
            aula_referente=aula_referente,
            user=usuario
        )
    except NameError:
        print('erro ao postar comentário')
