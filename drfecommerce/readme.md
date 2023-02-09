py django-admin-commands []: # Description: Django Admin Commands
py django-admin-startproject 
py manage.py runserver
def get_random_secret_key():
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return get_random_string(50, chars)
 interactive django shell
py manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
pip install -r requirements.txt