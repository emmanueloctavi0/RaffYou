
# Django
from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

# Utils
import requests


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email is required')
    
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """User model with email authentication"""
    email = models.EmailField(
        _('email address'),
        unique=True
    )

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        blank=True,
        null=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    facebook_id = models.CharField(
        _('ID de Facebook'),
        max_length=250,
        unique=True,
        null=True
    )

    profile_picture = models.ImageField(
        _('Foto de perfil'),
        upload_to='images/users',
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save_profile_picture(self, url_picture):
        """Save the profile picture from facebook"""
        res = requests.get(url_picture)
        picture = ContentFile(res.content)
        self.profile_picture.delete()
        self.profile_picture.save(
            f'{self.facebook_id}.jpeg',
            picture
        )
