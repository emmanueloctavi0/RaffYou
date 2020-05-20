
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import Provider
from django.contrib.auth import get_user_model


User = get_user_model()


class Score(BaseModel):
    class Rate(models.IntegerChoices):
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

    rate = models.IntegerField(
        _('Calificación'),
        choices=Rate.choices,
        default=Rate.START_1
    )

    comment = models.TextField(
        _('Comentario'),
        max_length=300,
        blank=True
    )

    def __str__(self):
        return f'{self.comment[:10]}... - {self.rate}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'provider'],
                name='unique_comment_by_user'
            )
        ]
