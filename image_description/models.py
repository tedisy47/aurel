from django.db import models

# Create your models here.
# models.py 
class Images(models.Model): 
	images = models.ImageField(upload_to='images/')