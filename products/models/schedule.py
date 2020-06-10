
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import Provider


class ScheduleDay(BaseModel):

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE
    )

    class Days(models.IntegerChoices):
        MONDAY = 0, _('Lunes')
        TUESDAY = 1, _('Martes')
        WEDNESDAY = 2, _('Miércoles')
        THURSDAY = 3, _('Jueves')
        FRIDAY = 4, _('Viernes')
        SATURDAY = 5, _('Sábado')
        SUNDAY = 6, _('Domingo')

    name = models.IntegerField(
        _('Día de la semana'),
        choices=Days.choices,
        default=Days.MONDAY
    )

    start_time = models.TimeField(
        _('Hora de inicio'),
        null=True
    )

    end_time = models.TimeField(
        _('Hora final'),
        null=True
    )

    is_active = models.BooleanField(
        _('Activo'),
        default=True
    )

    def __str__(self):
        return f'{self.name}: {self.start_time}-{self.end_time}'
