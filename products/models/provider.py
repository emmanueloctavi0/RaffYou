
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Models
from core.models import AddressBaseModel, BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Provider(BaseModel):
    """Provider model. A provider"""
    name = models.CharField(
        _('Nombre'),
        max_length=255,
        unique=True
    )

    description = models.TextField(
        _('Descripción'),
        blank=True
    )

    image = models.ImageField(
        upload_to='images/providers',
        blank=True
    )

    rate = models.ManyToManyField(
        User,
        through='Score',
        related_name='score_provider_set',
        blank=True
    )

    keywords = models.CharField(
        _('Palabras clave de búsqueda'),
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(
        _('Proveedor activo'),
        default=True
    )

    order = models.IntegerField(
        _('Orden en el que deberían aparecer los proveedores'),
        default=1
    )

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    @property
    def comments(self):
        """Return all comments and score"""
        return self.score_set.all()

    @property
    def score(self):
        """Return the provider rate"""
        score = self.score_set.aggregate(
            models.Avg('rate')
        )['rate__avg']

        if not score:
            return 5, 5

        return int(score), score

    @property
    def first_address(self):
        return self.provideraddress_set.first()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Proveedor')
        verbose_name_plural = _('Proveedores')

        ordering = ['order']


class ProviderAddress(AddressBaseModel):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.provider.name} - {self.zip_code}'


@receiver(pre_save, sender=Provider)
def handler_is_active(sender, instance, **kwargs):
    """When a provider is inactive all their products change to inactive"""
    try:
        current_instance = sender.objects.get(id=instance.id)
        if instance.is_active != current_instance.is_active:
            products = instance.product_set.all().update(
                is_active=instance.is_active
            )
    except instance.DoesNotExist:
        pass
