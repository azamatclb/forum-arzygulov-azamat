from django.conf import settings
from django.db import models


class Topic(models.Model):
    summary = models.CharField(max_length=300, verbose_name="Описание")
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата добавления")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='topics', default=1)

    def __str__(self):
        return f"{self.summary} {self.date_created}"

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
