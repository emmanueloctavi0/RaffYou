
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import Provider
from django.contrib.auth import get_user_model


User = get_user_model()


class Score(BaseModel):
    class Qualification(models.IntegerChoices):
        START_1 = 1, _('Pésimo')
        START_2 = 2, _('Malo')
        START_3 = 3, _('Bueno')
        START_4 = 4, _('Muy bueno')
        START_5 = 5, _('Excelente')

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE
    )

    qualification = models.IntegerField(
        _('Calificación'),
        choices=Qualification.choices,
        default=Qualification.START_1
    )

    comment = models.TextField(
        _('Comentario'),
        max_length=300,
        blank=True
    )
