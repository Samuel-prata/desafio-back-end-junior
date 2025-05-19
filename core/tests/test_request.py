from django.test import TestCase
from django.urls import reverse
import time

class StudentRequestTest(TestCase):
    
    def test_get_100_requests(self):
        url = reverse('student-list')
        start = time.time()
        for _ in range(100):
            response = self.client.get(url)
        end = time.time()
        time_requests = (end - start) / 10
        print(f"Average time for GET request: {time_requests:.4f} seconds")
        self.assertFalse(time_requests > 0.2)