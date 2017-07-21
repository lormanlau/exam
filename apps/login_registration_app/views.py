# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'login_registration_app/index.html')

def register(request):
	if request.method == "POST":
		Users.objects.validate(request.POST)
	return redirect('/')

def dashboard(request):
	return render(request, 'login_registration_app/dashboard.html')

def userinfo(request, id):
	return render(request, 'login_registration_app/user_info.html')