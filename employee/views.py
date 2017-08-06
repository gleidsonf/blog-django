from django.shortcuts import render
from .models import Doctor
# Create your views here.

def doctor_info(request):
	doctors = Doctor.objects.all().order_by('-id')
	return render(request, 'employee/doctor_info.html', {'doctors': doctors})