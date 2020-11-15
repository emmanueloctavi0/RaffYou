
# Django
from django.views.generic import TemplateView

# Utilities
import requests


class PageNotFoundView(TemplateView):
    template_name = 'core/404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resp = requests.get('https://api.giphy.com/v1/stickers/random?api_key=Exd7luYR5u2Z5132kzDzij8wFoIL5TaM&tag=fail&rating=g')

        try:
            url_gif = resp.json()['data']['images']['original']['webp']
        except (KeyError, TypeError):
            url_gif = 'https://media.giphy.com/media/EXHHMS9caoxAA/source.gif'

        context['url_gif'] = url_gif
        return context
