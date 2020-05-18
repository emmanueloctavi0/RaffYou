
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Models
from core.models import BaseModel


User = get_user_model()


class GeneralComment(BaseModel):
    """An opinion about the website and products"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    name = models.CharField(
        _('Nombre del usuario'),
        max_length=150
    )

    comment = models.TextField(
        _('Comentario / opinion')
    )

    def __str__(self):
        return self.name
