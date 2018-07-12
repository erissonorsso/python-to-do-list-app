from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'novo-usuario/', views.add_user, name='add_user'),
    path(r'login-usuario/', views.user_login, name='user_login'),
    path(r'logout-usuario/', views.user_logout, name='user_logout'),
    path(r'alterar-senha/', views.change_password, name='change_password'),
]
