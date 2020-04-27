
# Django
from django.conf import settings

import requests
from base64 import b64encode
from urllib.parse import urlencode


def get_tokens(code):
    """Get access and refresh token Facebook"""

    params = urlencode({
        'client_id': settings.AUTH_CLIENT_ID,
        'redirect_uri': settings.AUTH_REDIRECT_URI,
        'client_secret': settings.AUTH_CLIENT_SECRET,
        'code': code
    })

    url = settings.AUTH_TOKEN_URL

    url = f'{url}?{params}'

    response = requests.get(url)

    return response


def get_user_info(response):
    """Get the user info"""
    access_token = response['access_token']

    url = 'https://graph.facebook.com/me/'
    params = urlencode({
        'access_token': access_token,
        'fields': 'first_name,last_name,email,picture,id',
    })
    url = f'{url}?{params}'
    res = requests.get(url)
    return res
