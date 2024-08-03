from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

User = get_user_model()


class Profile(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", verbose_name="Аватарка")

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    groups = models.ManyToManyField(
        Group,
        related_name='profile_set',
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь.',
        verbose_name='Группы'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='profile_set',
        blank=True,
        help_text='Конкретные права доступа для этого пользователя.',
        verbose_name='Права доступа'
    )
