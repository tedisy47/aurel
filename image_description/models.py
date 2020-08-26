from django.db import models

# Create your models here.
# models.py 
class Images(models.Model): 
	images = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

class Kamus(models.Model):
	bugis = models.CharField(max_length=225)
	indonesia = models.CharField(max_length=225)
		