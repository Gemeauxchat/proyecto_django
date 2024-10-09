from django.utils.crypto import get_random_string

def make_random_password(length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return get_random_string(length, allowed_chars)