from django.test import TestCase
from django.urls import reverse
from ...models.student_model import Student


class StudentPostViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('student-create')
        self.valid_data = {
            'name': 'Samuel Silverio',
            'email': 'samuel@gmail.com',
            'cpf': '12345678901',
            'phone': '1234567890',
            'address': 'Rua paraiso, 112',
            'date_of_birth': '2000-01-01'
        }
        
    def test_post_request(self):
        self.client.post(self.url, data=self.valid_data)
        self.assertEqual(Student.objects.count(), 1)
        
        