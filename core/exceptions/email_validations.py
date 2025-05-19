from django.core.exceptions import ValidationError

class EmailValidation:
    
    def __init__(self, email):
        self.email = email 
        
    def validation_format(self, email):
        if '@' not in email and '.' not in email:
            raise ValidationError("Email inválido.")
        
    def validate(self):
        self.validation_format(self.email)
        return self.email.lower()
        
        