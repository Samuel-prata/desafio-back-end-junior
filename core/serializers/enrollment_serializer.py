from rest_framework import serializers
from ..models.enrollment_model import Enrollment
from ..serializers.student_serializer import StudentSerializer
from ..serializers.course_serializer import CourseSerializer

class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrollment_date', 'status']

class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Enrollment
        fields = ['id', 'student', 'course', 'enrollment_date', 'status']