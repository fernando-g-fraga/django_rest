from rest_framework import viewsets,generics
from escola.models import Aluno,Curso, Matricula
from escola.serializer import Aluno_Serializer, Curso_Serializer, Matricula_Serializer, ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 

class Alunos_viewset(viewsets.ModelViewSet):
    """Exibir todos os alunos cadastrados"""

    queryset = Aluno.objects.all()
    serializer_class = Aluno_Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class Cursos_viewset(viewsets.ModelViewSet):
    """Exibir todos os cursos cadastrados"""

    queryset = Curso.objects.all()
    serializer_class = Curso_Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Matriculas_viewset(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = Matricula_Serializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    '''Listando Matriculas do Aluno'''
    def get_queryset(self):
        query_set = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados (generics.ListAPIView):
    '''Listando Alunos Matriculados no curso'''
    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        
        
        return query_set
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


