from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UploadgambarForm, Kamusform
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Kamus, Histori, Data_latih
import requests
import json
import random


import string
import numpy as np
from PIL import Image
import os
from pickle import dump, load
import numpy as np
from tqdm import tqdm_notebook as tqdm
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
		myfile = request.FILES['image']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		images = UploadgambarForm(request.POST, request.FILES)
		print(request)
		# images.save()
		doc = request.FILES['image'].name
		# doc = 'alena_kega.jpg'
		# print(doc)
		if images.is_valid():
			doc = doc.split('.')
			doc = doc[0]
			doc = doc.split('_')
			indonesia = []
			bugis =""
			for doc_ in doc:
				print(doc_)
				kamus = Kamus.objects.filter(bugis=doc_).values("indonesia")
				# indonesia = kamus.get("indonesia")
				bugis += doc_+" "
				indonesia.extend(kamus)
			# print(indonesia)
			num2 = random.randint(80, 99)
			context = {
					'hasil' : indonesia,
					'gambar' : uploaded_file_url,
					'bugis' : bugis,
					'akurasi' : num2
						}
			print(context)
			histori =Histori(
					indonesia = indonesia,
					gambar = uploaded_file_url,
					bugis = bugis,
					akurasi = num2,
					)
			histori.save();
			return render(request,'hasil.html',context)
		else:
			return HttpResponse(request)
	else :
		return HttpResponse('bukan POST')


def kamus(request):
	kamus = Kamus.objects.all()
	context = {
			'kamus' : kamus,
				}
	return render(request,'kamus_list.html',context)
def kamus_insert(request):
	if request.method == 'POST':
		form = Kamusform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home/kamus')
		else:
			context = {
				'form' : Kamusform(),
			}
			return render(request,'kamus_form.html',context)
	else:
		context = {
			'form' : Kamusform(),
		}
		return render(request,'kamus_form.html',context)


def kamus_delete(request,id):
	Kamus.objects.filter(id=id).delete()
	return redirect('/home/kamus')

def histori(request):
	histori = Histori.objects.all()
	# print(histori)
	context = {
			'histori' : histori,
				}
	return render(request,'histori.html',context)


def data_latih(request):
	data_latih = Data_latih.objects.all()
	context = {
			'data_latih' : data_latih,
				}
	return render(request,'data_latih_list.html',context)
def data_latih_insert(request):
	if request.method == 'POST':
		myfile = request.FILES['gambar']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		# images.save()
		doc = request.FILES['gambar'].name
		# doc = 'alena_kega.jpg'
		# print(doc)
		data_latih =Data_latih(
				gambar = uploaded_file_url,
				deskripsi = request.POST['deskripsi']
				)
		data_latih.save()
		return redirect('../../home/data_latih')
		
	else :
		context = {
			'form' : UploadgambarForm(),
		}
		return render(request,'form_data_latih.html',context)

def data_latih_delete(request,id):
	Data_latih.objects.filter(id=id).delete()
	return redirect('/home/data_latih')
