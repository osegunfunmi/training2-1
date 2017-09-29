# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.core.urlresolvers import reverse
#from django.db.models.signals import pre_save

#from django.utils.text import slugify

# Create your models here.
class Guest(models.Model):
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	email = models.EmailField(max_length=155)
	password = models.CharField(max_length=125)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	modified = models.DateTimeField(auto_now=True, editable=False)
	#slug = models.SlugField(unique=True)
	def __unicode__(self):
		return self.get_fullname()

	def get_fullname(self):
		return "%s %s" % (self.first_name, self.last_name)

	#def get_absolute_url(self):
		#return reverse ("guest:detail", kwargs="id=self.id")

	#def create_slug(instance, new_slug=None):
		##if new_slug is not None:
			#slug = new_slug
			#qs = Guest.objects.filter(slug=slug).order_by("-id")
			#exists = qs.exists()
			#if exists:
				#new_slug = "%s-%" %(slug, qs.first().id)
				#return create_slug(instance,new_slug=new_slug)
			#return slug
#def  pre_save_guest_receiver(sender, instance, *args, **kwargs):
	#if not instance.slug:
		#instance.slug = create_slug(instance)

#pre_save.connect(pre_save_guest_receiver, sender=Guest)


class Event(models.Model):
	event_name = models.CharField(max_length=200)
	description = models.TextField()
	event_date = models.DateTimeField(editable=True)
	location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	#facilitator = models.CharField(max_length=200)
	
    

	def __unicode__(self):
		return self.get_event_name()

	def get_event_name(self):
		return "%s %s" % (self.event_name, self.description)

       #def save(self, *args, **kwargs):
		#self.slug = slugify(self.name)
		#if not self.pk:
			#Email.send("Thank you for registering", "segunfunmi@gmail.com")
		#super(Profile, self).save(*args, **kwargs)
		#Dashboard.update("This application now has %s users" % 56)
		

		