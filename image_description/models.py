from django.db import models

# Create your models here.
# models.py 
class Images(models.Model): 
	images = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')

class Kamus(models.Model):
	bugis = models.CharField(max_length=225)
	indonesia = models.CharField(max_length=225)
		
class Histori(models.Model):
	gambar = models.CharField(max_length=225)
	bugis = models.CharField(max_length=225)
	indonesia = models.CharField(max_length=225)
	akurasi = models.IntegerField()		

class Data_latih(models.Model):
	gambar = models.CharField(max_length=225)
	deskripsi = models.CharField(max_length=225)

		