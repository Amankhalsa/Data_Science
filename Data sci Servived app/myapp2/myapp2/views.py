from django.shortcuts import render
from . import test_model

def home(request):
	return render(request,"index.html")

# def result(request):
# 	return render(request,"result.html")

def result(request):
	user_input_age=int(request.GET['age'])
	predction=test_model.fake_model(user_input_age)
	# user_input_age+=" is your age "
	return render(request,"result.html", {'myrel':predction})