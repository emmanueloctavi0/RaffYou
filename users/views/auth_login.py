
# Django
from django.shortcuts import redirect, HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model, login

# Utilities
from uuid import uuid4
from urllib.parse import urlencode
from users.utils import get_tokens, get_user_info


User = get_user_model()


def auth_login_view(request):
    """Build the Facebook login url"""
    # Set cookie
    auth_state = uuid4().hex
    request.session['auth_state'] = auth_state

    params = urlencode({
        'client_id': settings.AUTH_CLIENT_ID,
        # 'response_type': 'code',
        # 'scope': 'user-read-email',
        'redirect_uri': settings.AUTH_REDIRECT_URI,
        'state': auth_state,
    })

    url = f'{settings.AUTH_URL}?{params}'

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
        return redirect('users:signup')

    response = response.json()

    user_info = get_user_info(response).json()

    try:
        user = User.objects.get(
            facebook_id=user_info['id']
        )
        # Update user data
        user.first_name = user_info.get('first_name')
        user.last_name = user_info.get('last_name')
        user.email = user_info.get('email')
        login(request, user)
        return redirect('raffles:home')
    except User.DoesNotExist:
        # Create new user
        user = User.objects.create_user(
            first_name=user_info.get('first_name'),
            last_name=user_info.get('last_name'),
            facebook_id=user_info.get('id'),
            email=user_info.get('email'),
            password=uuid4().hex
        )

        login(request, user)
        return redirect('raffles:home')
