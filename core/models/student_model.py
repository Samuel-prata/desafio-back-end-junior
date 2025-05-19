from django.db import models
from django.utils import timezone
import uuid
class Student(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name