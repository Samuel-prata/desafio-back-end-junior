from rest_framework import generics
from ..models.enrollment_model import Enrollment
from ..serializers.enrollment_serializer import EnrollmentSerializer, EnrollmentCreateSerializer

class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
class EnrollmentCreateView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentCreateSerializer
    
class EnrollmentWithdrawalView(generics.UpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.status = 'inactive'
        instance.save()
        
class StudentByCourseView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Enrollment.objects.filter(course_id=course_id).select_related('student')
    
""" View para teste com o Generics"""
class EnrollmentCreateListView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentCreateSerializer