from django.db import models


class GuestbookEntry(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    author_email = models.EmailField(verbose_name='Email автора')
    content = models.TextField(verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Запись в гостевой книге'
        verbose_name_plural = 'Записи в гостевой книге'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author_name} - {self.created_at.strftime("%d.%m.%Y %H:%M")}'
