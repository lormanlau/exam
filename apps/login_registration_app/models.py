# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def validate(self, user_data):
		errors = {}
		
		for something in user_data:
			if len(something) < 3:
				errors['length'] = "Items can not be less than 3 characters"
		if not EMAIL_REGEX.match(user_data['email']):
			errors['email'] = "Invalid email"
		if user_data['pass'] != user_data['con_pass']:
			errors['password'] = "Password does not match"

		return errors
		

# Create your models here.
class Users(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	bday = models.DateField()

class Quote(models.Model):
	author = models.CharField(max_length=255)
	text = models.TextField()
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)