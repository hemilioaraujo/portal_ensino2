from django.urls import path
from portal_ensino.api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('hello-protected/', views.HelloViewProtected.as_view(), name='hello_protected'),
]
