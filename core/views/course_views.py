from rest_framework import generics
from ..models.course_model import Course
from ..serializers.course_serializer import CourseSerializer, CourseCreateSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

class CourseListOneView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Course.objects.filter(id=course_id)
    
    
""" View para teste com o Generics"""
class CourseCreateListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer