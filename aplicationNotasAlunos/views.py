from django.shortcuts import render
from    aplicationNotasAlunos.models import  Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    alunosChave ={
        'alunos': alunos
    }
    return render(request,'index.html',alunosChave)


def matricula(request, id):
    aluno = Aluno.objects.get(id=id)
    contextAluno ={
        'aluno':aluno
    }
    return render(request,'matricula.html',contextAluno)