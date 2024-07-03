from rest_framework import viewsets
from escola.models import Aluno,Curso, Matricula
from escola.serializer import Aluno_Serializer, Curso_Serializer, Matricula_Serializer

class Alunos_viewset(viewsets.ModelViewSet):
    """Exibir todos os alunos cadastrados"""

    queryset = Aluno.objects.all()
    serializer_class = Aluno_Serializer

class Cursos_viewset(viewsets.ModelViewSet):
    """Exibir todos os cursos cadastrados"""

    queryset = Curso.objects.all()
    serializer_class = Curso_Serializer

class Matriculas_viewset(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = Matricula_Serializer


