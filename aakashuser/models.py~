from django.db import models

# Create your models here.

class User (models.Model):
	tab_id = models.IntegerField()
	email_id = models.EmailField(max_length = 75)
	location = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	repassword = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return self.email_id

