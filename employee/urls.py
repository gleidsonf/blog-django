from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^doctors$', views.doctor_info),
]
