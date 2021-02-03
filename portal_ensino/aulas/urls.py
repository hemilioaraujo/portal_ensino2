from django.urls import path

from portal_ensino.aulas.views import aula
from portal_ensino.base.views import xpto

urlpatterns = [
    # XPTO
    path('proxima_aula/', xpto, name='proxima_aula'),
    path('aula_anterior/', xpto, name='aula_anterior'),
    path('exercicio/', xpto, name='exercicio'),
    path('reprovado/', xpto, name='reprovado'),
    path('deletar-comentario/<int:id>', xpto, name="deletar_comentario"),


    path('', aula, name='aula'),
]
