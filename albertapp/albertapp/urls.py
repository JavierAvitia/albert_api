from django.contrib import admin
from django.urls import include, path, re_path
from cc_api import views
from django.conf.urls import handler404,handler403,handler400,handler500

#
# Defaults
#
handler404 = 'cc_api.views.redirect_404'
handler403 = 'cc_api.views.redirect_404'
handler400 = 'cc_api.views.redirect_404'
handler500 = 'cc_api.views.redirect_500'

#
# URLs
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cc_api/', include('cc_api.urls')),
    path('', views.albert_home),
]