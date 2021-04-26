from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
	phone = models.CharField(max_length =20,null=True,blank=True)
	email = models.EmailField(unique=True,null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add =True)
	updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


