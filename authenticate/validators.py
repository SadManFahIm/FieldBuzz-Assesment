from django.core.exceptions import ValidationError


def validate_file(value):
    value= str(value)
    if value.endswith(".pdf") != True: 
        raise ValidationError("Only PDF Documents can be uploaded")
    else:
        return value
