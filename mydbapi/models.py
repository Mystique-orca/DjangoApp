from django.db import models

# Create your models here.

from django.db import models

class Credential(models.Model):
	userid = models.IntegerField(primary_key=True)
	username = models.CharField(max_length=50)
	passwordhash = models.CharField(max_length=256)

	def __str__(self):
		return self.username
