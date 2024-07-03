from rest_framework import serializers
from escola.models import Aluno,Curso,Matricula

class Aluno_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno 
        fields = ['id','nome','rg','cpf','data_nascimento']


class Curso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class Matricula_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

