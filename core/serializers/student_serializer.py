from rest_framework import serializers
from ..models.student_model import Student
from ..exceptions.cpf_validations import CPFValidation
from ..exceptions.email_validations import EmailValidation

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']
        


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    
    def validate_cpf(self, value):
        return CPFValidation(value).validate()
    
    def validate_email(self, value):
        return EmailValidation(value).validate()