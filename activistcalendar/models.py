from django.db import models
from django import forms
from django.contrib.auth import models as authmodels
from uuidfield import UUIDField

class ActivistGroup(models.Model):
    group_id = UUIDField(auto=True, unique=True)
    name = models.TextField()
    description = models.TextField()
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True)
    city = models.TextField()
    province = models.TextField()
    country = models.TextField(default="United States")
    group_url = models.URLField()

class ActivistInterest(models.Model):
    interest_id = UUIDField(auto=True, unique=True)
    interest_name = models.TextField(unique=True)

class ActivistEvent(models.Model):
    event_id = UUIDField(auto=True, unique=True)
    host_group = models.ForeignKey(ActivistGroup)
    date = models.DateField()
    time = models.TimeField()
    address_line1 = models.TextField()
    address_line2 = models.TextField(blank=True)
    city = models.TextField()
    province = models.TextField()
    country = models.TextField(default="United States")
    contact_email = models.EmailField(max_length=2048)
    event_url = models.URLField()
    description = models.TextField()

class Profile(authmodels.User):
    user_id = UUIDField(auto=True, unique=True)
    user_full_name = models.TextField()
    user_email = models.EmailField(max_length=2048, unique=True)
    phone_number = models.CharField(max_length=2048)
    website = models.URLField()
    personal_message = models.TextField()
    activist_groups = models.ManyToManyField(ActivistGroup)
    activist_events = models.ManyToManyField(ActivistEvent)
    activist_interests = models.ManyToManyField(ActivistInterest)
    date_created = models.DateField(auto_now=True, auto_now_add=True)


class OutsideContact(models.Model):
    contact_id = UUIDField(auto=True, unique=True)
    contact_name = models.CharField(max_length=2048)
    contact_email = models.EmailField(max_length=2048)
    contact_subject = models.CharField(max_length=2048)
    contact_message = models.TextField()
