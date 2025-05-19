from rest_framework import serializers
from ..models.course_model import Course
from ..exceptions.data_course_validations import DataCourseValidation

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code_course']

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
    def validate_code_course(self, value):
      """Valida o código do curso no formato esperado"""
      return DataCourseValidation(value).validate()