from django.urls import path, re_path
from . import views

urlpatterns = [
	path('validate_cc/', views.validate_cc, name='validate_cc'),
	path('get_mii/', views.get_mii, name='get_mii'),
	path('get_iin/', views.get_iin, name='get_iin'),
	path('get_acc_num/', views.get_account_number, name='get_account_number'),
	path('get_check_digit/', views.get_check_digit, name='get_check_digit'),
    path('', views.albert_home, name='albert_home'),
]