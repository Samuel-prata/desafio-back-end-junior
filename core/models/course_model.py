from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code_course = models.CharField(max_length=20)
    start_date = models.DateField()
    

    def __str__(self):
        return self.name