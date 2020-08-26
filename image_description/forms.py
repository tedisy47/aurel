from django import forms 
from .models import *

class UploadgambarForm(forms.Form):
	model = Images
	image = forms.FileField(label='Gambar')
	

class Kamusform(forms.ModelForm):
	class Meta:
		model = Kamus
		fields = ['bugis', 'indonesia']
	bugis = forms.CharField(
        label = "Bahasa Bugis",
        max_length = 80,
        required = True,
    )
	indonesia = forms.CharField(
		label='Bahasa Indonesia',
        required = True,
        )