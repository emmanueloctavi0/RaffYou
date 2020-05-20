
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import AddressBaseModel, BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Provider(BaseModel):
    """Provider model. A provider"""
    name = models.CharField(
        _('Nombre'),
        max_length=100,
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
        blank=True
    )

    @property
    def comments(self):
        """Return all comments and score"""
        return self.score_set.all()

    @property
    def first_address(self):
        return self.provideraddress_set.first()

    def __str__(self):
        return self.name


class ProviderAddress(AddressBaseModel):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.provider.name} - {self.zip_code}'
