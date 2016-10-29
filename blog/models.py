from django.db import models
from django.utils import timezone 

# Create your models here.
class Article (models.Model):
	author=models.ForeignKey('auth.User') 
	Title=models.CharField(max_length = 25) 
	Body=models.CharField(max_length = 250)
	Conclussion=models.CharField(max_length = 100) 
	publishedDate=models.DateTimeField('Date Published') 
	def __str__(self):
		return self.Title


# Create your models here.
class Poll (models.Model):
	Comment=models.CharField(max_length = 15) 
	Like=models.CharField(max_length = 200)
	def __str__(self):
		return self.Comment