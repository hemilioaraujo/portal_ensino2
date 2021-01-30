from django.urls import path, include
from portal_ensino.base.views import home, xpto

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('', xpto, name='atualizar_usuario'),
    path('', xpto, name='novo_usuario'),
    path('', xpto, name='exibir_profile'),
    path('', xpto, name='aula'),
    path('', xpto, name='sobre'),

    # LOGIN
    path('contas/', include('django.contrib.auth.urls')),
]
