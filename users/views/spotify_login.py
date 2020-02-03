
# Django
from django.shortcuts import redirect, HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model, login

# Utilities
from uuid import uuid4
from urllib.parse import urlencode
from users.utils import get_tokens, get_user_info


def spotify_login_view(request):
    """Build the spotify login url"""
    # Set cookie
    auth_state = uuid4().hex
    request.session['auth_state'] = auth_state

    params = urlencode({
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'scope': 'user-read-email',
        'redirect_uri': settings.SPOTIFY_REDIRECT_URI,
        'state': auth_state,
    })

    url = 'https://accounts.spotify.com/authorize?' + params

    return redirect(url)


def callback_view(request):
    """Spotify authentication"""
    state = request.GET.get('state')
    error = request.GET.get('error')
    code = request.GET.get('code')

    auth_state = request.session.get('auth_state')

    if not state or auth_state != state:
        return HttpResponse("state doesn't exists")

    if error:
        return redirect('users:signup')

    # Request access and refresh token
    response = get_tokens(code)

    if response.status_code != 200:
        return response('users:signup')

    response = response.json()

    user_info = get_user_info(response).json()

    email = user_info['email']
    first_name = user_info['display_name']

    user = get_user_model().objects.filter(
        email=email
    ).first()

    if user:
        login(request, user)
        return redirect('raffles:home')
    
    user = get_user_model().objects.create_user(
        username=first_name,
        first_name=first_name,
        password=uuid4().hex,
        email=email
    )

    login(request, user)
    return redirect('raffles:home')
