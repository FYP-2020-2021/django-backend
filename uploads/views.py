from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserUploadForm
from .models import UserUpload
# Create your views here.

from django.http import HttpResponse, JsonResponse
from model.classifier import *

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

import sys

@csrf_exempt 
def upload_files(request):
	print("Uploading files...")
	if request.method == 'POST':
		form = UserUploadForm(request.POST, request.FILES)
		files = request.FILES.getlist('file')
		upload_results = []
		if form.is_valid():
			if len(files) == 0:
				return HttpResponse("Please indicate upload file field as 'file'", status=400)

			print(sys.path)
			arr_of_texts = []
			for f in files:
				print(f"From views.py for {f}: Running model...")
				text = f.read().decode('utf-8')
				arr_of_texts.append(text)

			results = run_model(arr_of_texts)
			upload_results = {}
			for i in range(len(results)):
				upload_results[file[i]] = results[i]
			
			return JsonResponse(upload_results, safe=False)

	return Response("Unable to upload files", status=status.HTTP_403_FORBIDDEN)



# for f in files:
# 	text = f.read().decode('utf-8')
# 	result, percentages = run_model(text)
# 	user_result = {
# 		"result": result,
# 		"percentages": percentages
# 	}
# 	upload_results.append(user_result)