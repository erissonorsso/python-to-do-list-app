"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from todo.core import views

from todo.tarefas import urls as tarefas_urls
from todo.accounts import urls as accounts_urls

urlpatterns = [
    path(r'', views.home, name='core'),
    re_path(r'tarefas/', include(tarefas_urls), name='tarefas'),  #Incluir o re_path e alterei o namespace para name
    re_path(r'accounts/', include(accounts_urls), name='accounts'),
    path('admin/', admin.site.urls),
]
