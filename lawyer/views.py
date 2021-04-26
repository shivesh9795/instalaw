from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import  authenticate, login as auth_login
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token


# Create your views here.


class UserRegistration(APIView):

	def post(self, request):
		data = request.data
		user_create = CustomUser.objects.create(first_name = data.get('first_name'),
			last_name = data.get('last_name'),
			phone = data.get('phone'),
			email = data.get('email'),
			username = data.get("username"))

		serializer = CustomUserSerializer(user_create)
		# if user_create:
		# 	token = Token.objects.create(user=user)
		return Response(serializer.data, status = status.HTTP_201_CREATED)
