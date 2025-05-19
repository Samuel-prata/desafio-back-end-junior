from django.core.exceptions import ValidationError
import re

class DataCourseValidation:
    
    def __init__ (self, value):
        self.value = value
        
    def validate_code_course(self):
        if not re.match(r'^[A-Z]{4}[0-9]{4}$', self.value):
            raise ValidationError(f'O código {self.value} não se enquadra no padrão esperado. Utilize uma abreviação. Ex: Fullstack Be-digial 2025 = FSBE2025')
        
    def validate(self):
        self.validate_code_course()
        return self.value