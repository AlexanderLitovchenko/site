from django.db import models


class Campaign(models.Model):

	camp_name = models.CharField(max_length = 25, verbose_name='Название')

	def __str__(self):
		return self.camp_name

	class Meta:
		verbose_name = 'Кампания'
		verbose_name_plural = 'Кампании'

	def get_absolute_url(self):
		return self.pk


class People(models.Model):

	name = models.CharField(max_length = 25, verbose_name='Имя')
	surname = models.CharField(max_length = 25, verbose_name='Фамилия')
	patr = models.CharField(max_length = 25, verbose_name='Отчество')
	email = models.EmailField(verbose_name='Почта')
	to_camp = models.ForeignKey(Campaign, on_delete = models.CASCADE, verbose_name='Кампания')

	def __str__(self):
		return self.name + ' ' + self.surname

	class Meta:
		verbose_name = 'Человек'
		verbose_name_plural = 'Люди'

	def get_absolute_url(self):
		return self.pk


class Houses(models.Model):

	city = models.CharField(max_length = 25, verbose_name='Город')
	street = models.CharField(max_length = 25, verbose_name='Улица')
	number = models.IntegerField(verbose_name='Номер дома')
	doors = models.IntegerField(verbose_name='Кол-во подъездов')
	flats = models.IntegerField(verbose_name='Кол-во квартир')
	to_camp = models.ForeignKey(Campaign, on_delete = models.CASCADE, verbose_name='Кампания')

	def __str__(self):
		city = self.city
		street = self.street
		number = self.number
		return f'{city}, {street} {number}'

	class Meta:
		verbose_name = 'Дом'
		verbose_name_plural = 'Дома'

	def get_absolute_url(self):
		return self.pk