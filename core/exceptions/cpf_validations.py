from django.core.exceptions import ValidationError

class CPFValidation:
    def __init__(self, cpf):
        self.cpf = cpf 
    
    def validation_length(self, cpf):
        if len(cpf) != 11:
            raise ValidationError("CPF deve conter 11 dígitos.")
    
    def validation_digits(self, cpf):
        if not cpf.isdigit():
            raise ValidationError("CPF deve conter apenas números.")
    
    def validate(self):
        self.validation_length(self.cpf)
        self.validation_digits(self.cpf)
        return self.cpf