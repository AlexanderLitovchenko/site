from django.db import models
from django.contrib.auth.models import User


class Users(User):
	date_of_birth = models.DateField(null = True, verbose_name = 'Дата рождения')
	phone = models.IntegerField(null = True, verbose_name = 'Номер телефона')
