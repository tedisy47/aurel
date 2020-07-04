from django import forms 
from .models import *

class UploadgambarForm(forms.Form):
	model = Images
	# fields = ['image']
	image = forms.FileField(label='Gambar')