from django.urls import path
from . import views

app_name = 'acervo'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('acervos/', views.lista_acervos, name='lista_acervos'),
    path('acervos/<int:pk>/', views.detalhe_acervo, name='detalhe_acervo'),
    path('acervos/novo/', views.criar_acervo, name='criar_acervo'),
    path('acervos/<int:pk>/editar/', views.editar_acervo, name='editar_acervo'),
    path('acervos/<int:pk>/deletar/', views.deletar_acervo, name='deletar_acervo'),
]
