from django.db import models
from django.contrib.auth.models import User


class Women(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_published = models.BooleanField(default=True)
	cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
	user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Женщина'
		verbose_name_plural = 'Женщины'


class Category(models.Model):
	title = models.CharField(max_length=255, db_index=True, unique=True)

	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
