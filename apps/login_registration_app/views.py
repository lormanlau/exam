# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import * 
import bcrypt

# Create your views here.
def index(request):
	if request.session['user_id'] != 0:
		return redirect('/quotes')
	return render(request, 'login_registration_app/index.html')

def register(request):
	if request.method == "POST":
		errors = Users.objects.validate(request.POST)
		if errors:
			for tags, error in errors:
				messages.error(request, error, extra_tags = tags)
		else:
			if len(Users.objects.filter(email = request.POST['email'])) > 0:
				messages.error(request, "Email is already taken" , extra_tags = "email")
			else:
				hashed_pw = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
				user = Users.objects.create(name = request.POST['name'], alias = request.POST['alias'], email= request.POST['email'], password = hashed_pw, bday = request.POST['bday'])
				request.session['user_id'] = user.id
				request.session['user_alias'] = user.alias
				return redirect('/quotes')
	return redirect('/')

def logout(request):
	request.session['user_id'] = 0
	return redirect('/')

def login(request):
	user = Users.objects.filter(email = request.POST['email'])
	if user:
		if bcrypt.checkpw(request.POST['pass'].encode(), user.first().password.encode()):
			request.session['user_id'] = user.first().id
			request.session['user_alias'] = user.first().alias
			return redirect('/quotes')

	messages.error(request, "Invalid Email or Password" , extra_tags = "email")
	return redirect('/')

def dashboard(request):
	if request.session['user_id'] == 0:
		messages.error(request, "You are not Logged In", extra_tags = 'Not Logged in')
		return redirect('/')
	else:
		context = {
		'quotes': Quote.objects.all().order_by('-id')
		}
		return render(request, 'login_registration_app/dashboard.html', context)

def addquote(request):
	if request.method == "POST":
		errors = False
		if len(request.POST['name']) < 3:
			messages.error(request, "Author needs to be at least 3 letters long", extra_tags = 'author')
			errors = True
		if len(request.POST['text']) < 10:
			messages.error(request, "Message needs to be at least 10 letters long", extra_tags = 'text')
			errors = True

		if errors == False:
			Quote.objects.create(author = request.POST['name'], text = request.POST['text'], user = Users.objects.get(id = request.session['user_id']))

	return redirect('/quotes')

def userinfo(request, id):
	context = {
	'quotes': Quote.objects.filter(user = Users.objects.get(id = id)),
	'user': Users.objects.get(id = id),
	'numb_of_quotes': len(Quote.objects.filter(user = Users.objects.get(id = id)))
	}
	return render(request, 'login_registration_app/user_info.html', context)

def addfavorites(request, id):
	Favorites.objects.create(user = Users.objects.get(id = request.session.user_id), quote = Quote.objects.get(id = id))
	return redirect('/quotes')