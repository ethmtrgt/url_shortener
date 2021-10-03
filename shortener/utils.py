import random
from .models import ShortUrl
from string import ascii_letters

def _create_short_code(length: int=4):
    alias = ''
    letter_list = list(ascii_letters)
    for _ in range(length):
        random_letter = random.choice(letter_list)
        alias += random_letter
    return alias

def create_alias():
    is_available = False
    while not is_available:
        alias = _create_short_code()
        is_available = not ShortUrl.objects.filter(alias=alias).exists()
    return alias

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip