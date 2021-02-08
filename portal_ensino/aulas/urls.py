from django.urls import path
from portal_ensino.aulas.views import aula, proxima_aula, aula_anterior
from portal_ensino.base.views import xpto

urlpatterns = [
    # XPTO
    # path('proxima_aula/', xpto, name='proxima_aula'),
    # path('aula_anterior/', xpto, name='aula_anterior'),
    path('deletar-comentario/<int:id>', xpto, name="deletar_comentario"),

    path('', aula, name='aula'),
    path('proxima_aula/', proxima_aula, name='proxima_aula'),
    path('aula_anterior/', aula_anterior, name='aula_anterior'),
]
