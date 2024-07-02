from rest_framework import serializers
from escola.models import Aluno,Curso

class Aluno_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno 
        fields = ['id','nome','rg','cpf','data_nascimento']


class Curso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'



