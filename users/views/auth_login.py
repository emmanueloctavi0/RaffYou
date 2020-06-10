
# Django
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib import messages

# Utilities
from uuid import uuid4
from urllib.parse import urlencode
from users.utils import get_tokens, get_user_info

# Tasks
from users.tasks import send_email_html


User = get_user_model()


def auth_login_view(request):
    """Build the Facebook login url"""
    # Set cookie
    auth_state = uuid4().hex
    request.session['auth_state'] = auth_state

    params = urlencode({
        'client_id': settings.AUTH_CLIENT_ID,
        # 'response_type': 'code',
        'scope': 'public_profile,email',
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
        messages.error(request, 'Ha ocurrido un error inesperado.')
        return redirect('users:signup')

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
            email=user_info.get('email')
        )
        # Update user data
        user.first_name = user_info.get('first_name')
        user.last_name = user_info.get('last_name')
        user.email = user_info.get('email')
        user.save_profile_picture(user_info['picture']['data']['url'])
        login(request, user)
        return redirect('products:home')
    except User.DoesNotExist:
        # Create new user
        try:
            user = User.objects.create_user(
                first_name=user_info.get('first_name'),
                last_name=user_info.get('last_name'),
                facebook_id=user_info.get('id'),
                email=user_info.get('email'),
                password=uuid4().hex
            )
        except ValueError:
            messages.error(request, 
                ('Parece que tu cuenta de Facebook no cuenta con un correo electrónico, '
                'para nuestro servicio es necesario que nos lo proporciones. '
                '¡Estamos trabajando arduamente para que puedas unirte a nosotros de otras formas! '
                'Ponte en contacto a través de nuestra página de Facebook')
            )
            return redirect('products:home')

        user.save_profile_picture(user_info['picture']['data']['url'])
        login(request, user)

        # Send email
        subject = '¡Bienvenido a Raffyou!'
        template = 'mails/welcome.html'
        from_email = 'Equipo Raffyou support@raffyou.com'
        to = user.email
        send_email_html.delay(subject, template, from_email, [to])
        return redirect('products:home')
