
# Django
from django.conf import settings

import requests
from base64 import b64encode


def get_tokens(code):
    """Get access and refresh token spotify"""
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.SPOTIFY_REDIRECT_URI
    }

    auth_client = '{}:{}'.format(
        settings.SPOTIFY_CLIENT_ID,
        settings.SPOTIFY_CLIENT_SECRET
    ).encode()

    headers = {
        'Authorization': 'Basic {}'.format(b64encode(auth_client).decode())
    }
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data=payload,
        headers=headers
    )

    return response


def get_user_info(response):
    """Get the user info"""
    access_token = response['access_token']

    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    res = requests.get('https://api.spotify.com/v1/me', headers=headers)
    return res
