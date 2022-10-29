from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        related_name='profiles',
        on_delete=models.CASCADE,
        verbose_name='User profile'
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Avatar'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of birth'
    )

    def __str__(self):
        return f'User profile {self.user.get_full_name()}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
