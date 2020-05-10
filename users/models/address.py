
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.db import models

# Models
from core.models import BaseModel


User = get_user_model()


class Address(BaseModel):
    """The User address"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(
        _('Nombre y apellido'),
        max_length=250
    )

    zip_code = models.CharField(
        _('Código postal'),
        max_length=10
    )

    state = models.CharField(
        _('Estado'),
        max_length=50
    )

    city = models.CharField(
        _('Delegación / Municipio'),
        max_length=255
    )

    colony = models.CharField(
        _('Colonia / Asentamiento'),
        max_length=255
    )

    street_name = models.CharField(
        _('Calle'),
        max_length=255
    )

    street_number = models.CharField(
        _('N° Exterior'),
        max_length=10
    )

    internal_number = models.CharField(
        _('N° Interior / Depto (opcional)'),
        max_length=10,
        blank=True
    )

    between_street1 = models.CharField(
        _('Calle 1'),
        max_length=255,
        blank=True
    )

    between_street2 = models.CharField(
        _('Calle 1'),
        max_length=255,
        blank=True
    )

    telephone = models.CharField(
        _('Teléfono de contacto'),
        max_length=20,
    )

    references = models.TextField(
        _('Indicaciones adicionales para entregar tus compras en esta dirección'),
        max_length=500
    )
