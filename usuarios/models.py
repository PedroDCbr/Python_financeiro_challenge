from django.contrib.auth.models import Permission
from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=150, db_index=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    permissoes = models.ManyToManyField(Permission, blank=True)
