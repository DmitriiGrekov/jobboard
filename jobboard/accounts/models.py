from django.db import models
from django.contrib.auth.models import AbstractUser
from jobs.models import JobModel, ResumeModel


class AdvUser(AbstractUser):
    """
        Своя модель пользователя
    """
    TYPE_USER_CHOICES = (
        ('employment', 'Работодатель'),
        ('applicant', 'Соискатель')
    )
    phone = models.CharField(max_length=20,
                             verbose_name='Телефон',
                             blank=True,
                             null=True
                             )
    avatar = models.ImageField(verbose_name='Аватар',
                               blank=True,
                               null=True)
    type_user = models.CharField(max_length=120,
                                 choices=TYPE_USER_CHOICES,
                                 default='applicant',
                                 verbose_name='Тип пользователя')
    favourits = models.ManyToManyField(JobModel,
                                       verbose_name='Избранные вакансии',
                                       related_name='favourits',
                                       blank=True,
                                       null=True)
    resume = models.ManyToManyField(ResumeModel,
                                    verbose_name='Отклики',
                                    blank=True,
                                    null=True)
    jobs = models.ManyToManyField(JobModel,
                                  related_name='job',
                                  verbose_name='Вакансии пользователя',
                                  blank=True,
                                  null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " -> " + self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
