from django.urls import path
from .views import *

urlpatterns = [
	# path('auth/login/',UserLogin.as_view(),name='login'),
	path('register/', UserRegistration.as_view()),
	# path('auth/logout/',UserLogout.as_view(),name='logout'),
 #    path('loginmember/',LoginMemberAPI.as_view(),name='loginmember'),


]