from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import UploadgambarForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import requests
import json


import string
import numpy as np
from PIL import Image
import os
from pickle import dump, load
import numpy as np
from keras.applications.xception import Xception, preprocess_input
from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers.merge import add
from keras.models import Model, load_model
from keras.layers import Input, Dense, LSTM, Embedding, Dropout
# small library for seeing the progress of loops.
from tqdm import tqdm_notebook as tqdm
# tqdm().pandas()
# Create your views here.

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
		# print(request)
		doc = request.FILES['image'].read();
		# if images.is_valid():
		# 	images.save()
		# 	return HttpResponse('ok')
		# else:
		# 	return HttpResponse(request)
		descriptions = load_descriptions(doc)
		print(descriptions)
		return HttpResponse(descriptions)
	else :
		return HttpResponse('bukan POST')


def load_descriptions(doc):
	mapping = dict()
	# process lines
	# print(doc)
	# for line in doc.split('\n'):
	# 	# split line by white space
	# 	tokens = line.split()
	# 	if len(line) < 2:
	# 		continue
	# 	# take the first token as the image id, the rest as the description
	# 	image_id, image_desc = tokens[0], tokens[1:]
	# 	# remove filename from image id
	# 	image_id = image_id.split('.')[0]
	# 	# convert description tokens back to string
	# 	image_desc = ' '.join(image_desc)
	# 	# create the list if needed
	# 	if image_id not in mapping:
	# 		mapping[image_id] = list()
	# 	# store description
	# 	mapping[image_id].append(image_desc)
	return mapping