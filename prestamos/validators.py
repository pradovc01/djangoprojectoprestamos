from django.core.exceptions import ValidationError
from string import ascii_letters, digits


def validar_positivos(value):
    if value<1:
        raise ValidationError(f'{value} no es positivo.')

def validar_string(value):
    if set(value).difference(ascii_letters + digits):
        raise ValidationError(f'{value} has specia characteres.')
