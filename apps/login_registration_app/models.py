# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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