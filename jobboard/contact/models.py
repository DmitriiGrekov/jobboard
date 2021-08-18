from django.db import models


class ContactMessage(models.Model):
    """
        Модель сообщений обратной связи 
    """
    message = models.TextField(verbose_name='Текст письма')
    name = models.CharField(max_length=120, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    subject = models.CharField(max_length=120, verbose_name='Тема')
    readed = models.BooleanField(verbose_name='Прочтено?', default=False)
    sended_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от пользователя {self.name} -> {self.email}"

    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения от пользователей'