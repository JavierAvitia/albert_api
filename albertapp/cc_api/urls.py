from django.urls import path, re_path

from . import views

urlpatterns = [
	re_path(r'^validate_cc/(?P<cc_num>[0-9]+)/$', views.validate_cc, name='validate_cc'),
	re_path(r'^get_mii/(?P<cc_num>[0-9]+)/$', views.get_mii, name='get_mii'),
	re_path(r'^get_iin/(?P<cc_num>[0-9]+)/$', views.get_iin, name='get_iin'),
	re_path(r'^get_acc_num/(?P<cc_num>[0-9]+)/$', views.get_account_number, name='get_account_number'),
	re_path(r'^get_check_digit/(?P<cc_num>[0-9]+)/$', views.get_check_digit, name='get_check_digit'),
    path('', views.albert_home, name='albert_home'),
]