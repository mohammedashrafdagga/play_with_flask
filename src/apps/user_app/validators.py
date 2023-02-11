from wtforms import ValidationError


def custom_username_valid(form, field):
    print(field.data)
    if len(field.data) < 10:
        raise ValidationError(message='The length of this filed is less 5 characters')
        
    return True