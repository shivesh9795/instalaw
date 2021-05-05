from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import  authenticate, login as auth_login
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth import  authenticate, login as auth_login
from lawyer.tasks import *


# Create your views here.


class UserRegistration(APIView):

	def post(self, request):
		data = request.data
		# user_create = CustomUser.objects.create(first_name = data.get('first_name'),
		# 	last_name = data.get('last_name'),
		# 	phone = data.get('phone'),
		# 	email = data.get('email'),
		# 	username = data.get("username"),
		# 	password = data.get("password"))

		# serializer = CustomUserSerializer(user_create)
		check.delay()
		# if user_create:
		# 	token = Token.objects.create(user=user)
		return Response("success", status = status.HTTP_201_CREATED)
class UserLogin(APIView):
	def post(self,request):

		if not request.data.get('email'):
			return Response({"error" : "Please provide email"}, status = status.HTTP_400_BAD_REQUEST)
		if not request.data.get('password'):
			return Response({"error" : "Please provide password"}, status = status.HTTP_400_BAD_REQUEST)

		if not CustomUser.objects.filter(email=request.data['email']).exists():
			return Response({"error" : "Email does't exists"}, status = status.HTTP_400_BAD_REQUEST)
		
		else:
			user = CustomUser.objects.get(email=request.data['email'])		
		if not user.check_password(request.data['password']):
			return Response({"error" : "incorrect password"}, status = status.HTTP_401_BAD_REQUEST)			
		auth_user = authenticate(email=request.data['email'], password=request.data['password'])
		token , created = Token.objects.get_or_create(user=user)
		return Response({"key":token.key,"is_lawyer": str(user.email)},status=status.HTTP_200_OK)



class  UserLogout(APIView):
	def post(self,request):
		email = request.data.get("email")
		print(email)
		user = Token.objects.get(user = (email)).key
		print(user)
		user.delete()
		return Response({"detail":"Successfully logged out."} , status = status.HTTP_200_OK)

@api_view(['GET'])
def lawyerOverview(request):
	lawyer_urls = {
		'List' : '/lawyer-list/',
		'Detail View' : '/lawyer-detail/<int:id>/',
		'Create' : '/lawyer-create/',
		'Update' : '/lawyer-update/<int:id>/',
		'Delete' :	 '/lawyer-Delete/<int:id>/'
		}
	return Response (lawyer_urls);



@api_view(['GET'])
def ShowAll(request,pk):
	customuser = CustomUser.objects.get(id=pk)
	serializer = CustomUserSerializer(customuser,many = True)
	return Response(serializer.data)


@api_view(['GET'])
def CreateLawyer(request):
	serializer = CustomUserSerializer(data = request.data)


	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def UpdateLawyer(request,pk):
	customuser = CustomUser.objects.get(id=pk)
	serializer = CustomUserSerializer(instance=customuser,data = request.data)


	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)





@api_view(['POST'])
def DeleteLawyer(request,pk):
	try:
		customuser = CustomUser.objects.get(id=pk)
		customuser.delete()
		return Response('Item delete sucessfuly')
	except:
		return Response({"error":"Item is recentaly deleted"})


def testemail(request) :
    subject="test email"
    message="hello sid"
    reply_to_list=['abc@gmail.com','def@gmail.com']

    send_mail(subject,message,'ant@a.com',reply_to_list,fail_silently=True)
