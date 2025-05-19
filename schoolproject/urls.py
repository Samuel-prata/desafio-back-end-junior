from django.contrib import admin
from django.urls import path
from core.views import student_views, course_views, enrollment_views, schema_view

urlpatterns = [
    path("swagger/", schema_view.schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    
    path("courses/", course_views.CourseListView.as_view(), name="course-list"),
    path("courses/<int:course_id>/", course_views.CourseListOneView.as_view(), name="course-one-list"),
    path("courses/<int:course_id>/students/", enrollment_views.StudentByCourseView.as_view(), name="student-enrollment-list"),
    path("courses/new/", course_views.CourseCreateView.as_view(), name="course-create"),
    
    path("students/", student_views.StudentListView.as_view(), name="student-list"),
    path("students/<uuid:student_id>/", student_views.StudentListOneView.as_view(), name="student-detail"),
    path("students/register/", student_views.StudentCreateView.as_view(), name="student-create"),
    
    path("enrollments/", enrollment_views.EnrollmentListView.as_view(), name="enrollment-list"),
    path("enrollments/do-enrollment/", enrollment_views.EnrollmentCreateView.as_view(), name="enrollment-create"),
    path("enrollments/<int:pk>/", enrollment_views.EnrollmentWithdrawalView.as_view, name="Withdrawal-enrollment"),
    
    # Urls para teste com o Generics 
    path("courses/test_generics/", course_views.CourseCreateListView.as_view(), name="course-list-create"),
    path("students/test_generics/", student_views.StudentCreateListView.as_view(), name="student-list-create"),
    path("enrollments/test_generics/", enrollment_views.EnrollmentCreateListView.as_view(), name="enrollment-list-create"),
]