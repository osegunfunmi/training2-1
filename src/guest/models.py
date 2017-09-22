# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Guest(models.Model):
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	email = models.EmailField(max_length=155)
	password = models.CharField(max_length=125)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True, editable=False)
	def __unicode__(self):
		return self.get_fullname()

	def get_fullname(self):
		return "%s %s" % (self.first_name, self.last_name)