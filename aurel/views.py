from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from image_description.forms import UploadgambarForm
# import requests
import json
# Create your views here.

def index(request):

	
	context = {
		'form' : UploadgambarForm(),
	}
	return render(request,'form_.html',context)


def login(requests):
	# print(requests)
	# return HttpResponse(requests)
	if requests.method == 'POST':
		# print(requests)
		user = authenticate(username=requests.POST['username'], password=requests.POST['password'])
		if user is not None:
			if user.is_active is True:
				auth_login(requests, user)
				messages.add_message(requests, messages.INFO, 'Selamat datang.')
				return redirect('/home/')
				# return HttpResponse('ok')
	else:
		return redirect('/welcome/')



def welcome(request):
	return render(request,'login.html')

def logout(request):
	auth_logout(request)
	return redirect('login')
	# return HttpResponse('kk')
