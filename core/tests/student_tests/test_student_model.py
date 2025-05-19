from django.test import TestCase
from ...models.student_model import Student

class StudentTestCase(TestCase):
    def setUp(self):
        
        self.student = Student.objects.create(
        name= "Naruto Uzumaki",
        email= "naruto@email.com",
        cpf= "98754123612",
        phone= "12981317865",
        address= "Rua Hokage",
        date_of_birth= "2001-10-10"
        )
    
    def test_student_creation(self):
        self.assertIsInstance(self.student, Student)
        self.assertFalse(self.student.email.rfind('@') == -1)
        self.assertFalse(self.student.cpf.count() != 11)
        