from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('М', 'М'),
    ('Ж', 'Ж')
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Номер телефона')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
