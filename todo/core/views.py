from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from todo.tarefas.models import Tarefa

# View para apresentacao das tarefas do usuario logado.
@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user)  #Idem a SELECT * FROM tarefa (´e o ORM do Django). Traz apenas as tarefas do user da sessao
    return render(request, 'core/index.html', {'tarefas': tarefas})
