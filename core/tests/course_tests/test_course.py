from django.test import TestCase
from ...models.course_model import Course
import re

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            code_course='TEST2023',
            start_date='2023-01-01'
        )

    def test_course_creation(self):
        self.assertIsInstance(self.course, Course)
        
    def test_creation_code_course(self):
        self.assertFalse(re.match(r'^[A-Z]{4}[0-9]{4}$', self.course.code_course) is None)