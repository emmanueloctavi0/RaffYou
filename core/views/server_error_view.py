
# Django
from django.shortcuts import render

# Utilities
import requests


def server_error(request):

    resp = requests.get('https://api.giphy.com/v1/stickers/random?api_key=Exd7luYR5u2Z5132kzDzij8wFoIL5TaM&tag=fail&rating=g')

    try:
        url_gif = resp.json()['data']['images']['original']['webp']
    except (KeyError, TypeError):
        url_gif = 'https://media.giphy.com/media/EXHHMS9caoxAA/source.gif'

    return render(
        request,
        template_name='core/500.html',
        context={
            'url_gif': url_gif,
        }
    )
