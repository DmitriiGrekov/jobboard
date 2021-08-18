from django.db import models


def user_directory_path(instance, filename):
    return f"portfolio/{instance.full_name}/{filename}"


class JobCategory(models.Model):
    """
        Модель категорий вакансий
    """
    name = models.CharField(max_length=120, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория вакансии'
        verbose_name_plural = 'Категории вакансии'


class JobModel(models.Model):
    """
        Модель вакансии
    """
    EMPLOYMENT_CHOICES = (
        ('p', 'Part-Time'),
        ('f', 'Full-Time'),
        ('s', 'Free-Shedule')
    )
    EXPERIENCE_CHOICES = (
        ('one', 'Less 1 YEAR'),
        ('one-three', 'From 1 to 3 YEARS'),
        ('more', 'More than 3 YEARS')
    )
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    title = models.CharField(max_length=120,
                             verbose_name='Заголовок')
    position = models.CharField(max_length=300,
                                verbose_name='Где находится')
    employment = models.CharField(max_length=120,
                                  verbose_name='Занятость',
                                  choices=EMPLOYMENT_CHOICES,
                                  default='Full-Time')
    description = models.TextField(verbose_name='Описание вакансии')
    category = models.ManyToManyField(JobCategory)
    experience = models.CharField(max_length=120,
                                  verbose_name='Опыт',
                                  choices=EXPERIENCE_CHOICES,
                                  default='From 1 to 3 YEARS')
    gender = models.CharField(max_length=120,
                              choices=GENDER_CHOICES,
                              verbose_name='Пол',
                              default='Male')
    responsibility = models.TextField('Ответственность',
                                      blank=True,
                                      null=True)
    qualifications = models.TextField(verbose_name='Квалификации',
                                      blank=True,
                                      null=True)
    benefits = models.TextField(verbose_name='Выгоды',
                                blank=True,
                                null=True)
    date_publish = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(verbose_name='Количество мест в вакансии',
                                  blank=True,
                                  null=True,
                                  default=1)
    salary_min = models.IntegerField(verbose_name='Минимальная зарплата')
    salary_max = models.IntegerField(verbose_name='Максимальная зарплата')
    image = models.ImageField(verbose_name='Лого вакансии')

    def __str__(self):
        return self.title + " -> " + self.position

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


class ResumeModel(models.Model):
    """
        Модель отклика на вакансию
    """
    full_name = models.CharField(max_length=120,
                                 verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    portfolio_link = models.CharField(max_length=1000,
                                      verbose_name='Ссылка на портфолио')
    portfolio_file = models.FileField(verbose_name='Портфолио',
                                      upload_to=user_directory_path,
                                      blank=True,
                                      null=True)
    coverletter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(JobModel,
                                on_delete=models.CASCADE,
                                verbose_name='Вакансия',
                                related_name='resume_user')

    def __str__(self):
        return 'Отклик на вакансию: ' + self.vacancy.title + " от пользователя: " + self.full_name

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class ResumeMessageModel(models.Model):
    """
        Модель комментария под отклик 
    """
    name = models.CharField(max_length=120,
                            verbose_name='Имя',
                            blank=True,
                            null=True)
    comment = models.TextField(verbose_name='Комментарий на отклик',
                               blank=True,
                               null=True)
    resume = models.ForeignKey(ResumeModel,
                               on_delete=models.CASCADE,
                               related_name='resume_message',
                               verbose_name='Отклик')
    date_publish = models.DateTimeField(auto_now_add=True,
                                        null=True,
                                        blank=True)

    def __str__(self):
        return f"Сообщение на отклик {self.resume.full_name}"

    class Meta:
        verbose_name = 'Сообщениe на отклик'
        verbose_name_plural = 'Сообщения на отклики'
