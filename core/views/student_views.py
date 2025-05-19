from rest_framework import generics
from ..models.student_model import Student
from ..serializers.student_serializer import StudentSerializer, StudentCreateSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    
class StudentListOneView(generics.ListAPIView):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Student.objects.filter(id=student_id)

""" View para teste com o Generics"""
class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer