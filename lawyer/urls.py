from django.urls import path
from .views import *
from .import views

urlpatterns = [
	path('auth/login/',UserLogin.as_view(),name='login'),
	path('register/', UserRegistration.as_view()),
	path('auth/logout/',UserLogout.as_view(),name='logout'),
 #    path('loginmember/',LoginMemberAPI.as_view(),name='loginmember'),
 	# path('overview/', lawyerOverview.as_view())
 	path('', views.lawyerOverview,name = 'lawyerOverview'),
 	path('lawyer-list/<int:pk>/', views.ShowAll,name = 'lawyer-list'),
 	path('lawyer-create/', views.CreateLawyer,name = 'lawyer-create'),

 	path('lawyer-update/<int:pk>/', views.UpdateLawyer,name = 'lawyer-update'),
 	path('lawyer-delete/<int:pk>/', views.DeleteLawyer,name = 'lawyer-delete'),
	path('lawyer-testemail/',views.testemail,name="testemail")



]