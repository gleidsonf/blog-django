from django.db import models
from django.utils import timezone

class Doctor(models.Model):
	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=70)
	specialty = models.CharField(max_length=30)

	def add(self):
		self.save()

	def __str__(self):
		return self.specialty
