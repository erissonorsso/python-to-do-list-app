from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path(r'nova-categoria/', views.nova_categoria, name='nova_categoria'),
    re_path(r'editar_categoria/(?P<id_categoria>[0-9]+)/', views.editar_categoria, name='editar_categoria'),
    re_path(r'delete_categoria/(?P<id_categoria>[0-9]+)/', views.delete_categoria, name='delete_categoria'),
    path(r'nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
    re_path(r'editar_tarefa/(?P<id_tarefa>[0-9]+)/', views.editar_tarefa, name='editar_tarefa'),
    re_path(r'delete-tarefa/(?P<id_tarefa>[0-9]+)/', views.delete_tarefa, name='delete_tarefa'),
]
