import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=10)
    email = models.EmailField(_('email address'), unique=True)
