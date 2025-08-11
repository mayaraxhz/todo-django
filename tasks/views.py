
from django.shortcuts import render, get_object_or_404
from .models import Tarefa

# Listar todas as tarefas
def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-data_criacao')
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

# Visualizar detalhes de uma tarefa
def visualizar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefas/visualizar_tarefa.html', {'tarefa': tarefa})
