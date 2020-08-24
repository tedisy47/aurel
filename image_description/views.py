from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UploadgambarForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Kamus
import requests
import json



def index(request):

	if not request.user.is_authenticated:
		return redirect('login')
    # print (request.user.id)
	else:
		context = {
			'form' : UploadgambarForm(),
		}
		return render(request,'image_upload.html',context)



def upload_image(request):
	if request.method == 'POST':
		images = UploadgambarForm(request.POST, request.FILES)
		print(request)
		doc = request.FILES['image'].name
		# doc = 'alena_kega.jpg'
		# print(doc)
		if images.is_valid():
			doc = doc.split('.')
			doc = doc[0]
			doc = doc.split('_')
			indonesia = []
			for doc_ in doc:
				print(doc_)
				kamus = Kamus.objects.filter(bugis=doc_).values("indonesia")
				# indonesia = kamus.get("indonesia")
				
				indonesia.extend(kamus)
			# print(indonesia)
			context = {
					'hasil' : indonesia,
						}
			return render(request,'hasil.html',context)
		else:
			return HttpResponse(request)
	else :
		return HttpResponse('bukan POST')


def kamus(request):
	