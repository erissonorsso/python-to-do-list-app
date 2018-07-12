from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from todo.tarefas.models import Tarefa

# Create your views here.

@login_required
def home(request):
    tarefas = Tarefa.objects.all()  #Idem a SELECT * FROM tarefa (´e o ORM do Django)
    return render(request, 'core/index.html', {'tarefas': tarefas})
