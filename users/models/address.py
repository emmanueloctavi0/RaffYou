
# Django
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

# Models
from core.models import AddressBaseModel


User = get_user_model()


class Address(AddressBaseModel):
    """The User address"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
