from django.urls import path
from portal_ensino.base.views import home

app_name = 'base'

urlpatterns = [
    path('', home, name='home')
]
