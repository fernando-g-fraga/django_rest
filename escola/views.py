from rest_framework import viewsets,generics
from escola.models import Aluno,Curso, Matricula
from escola.serializer import Aluno_Serializer, Curso_Serializer, Matricula_Serializer, ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosSerializer

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

class ListaMatriculasAluno(generics.ListAPIView):
    '''Listando Matriculas do Aluno'''
    def get_queryset(self):
        query_set = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados (generics.ListAPIView):
    '''Listando Alunos Matriculados no curso'''
    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        
        
        return query_set
    serializer_class = ListaAlunosMatriculadosSerializer


