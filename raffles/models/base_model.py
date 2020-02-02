
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Raffles base model"""
    created_at = models.DateTimeField(
        _('Fecha de creación'),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _('Fecha de modificación'),
        auto_now=True
    )

    class Meta:
        abstract = True
