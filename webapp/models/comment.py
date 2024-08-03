from django.conf import settings
from django.db import models
from django.urls import reverse


class Comment(models.Model):
    comment = models.TextField(max_length=500, verbose_name='Комментарий')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    topic = models.ForeignKey('Topic', on_delete=models.RESTRICT, verbose_name='Тема', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', default=1)

    def __str__(self):
        return f"{self.comment} {self.date_created}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
