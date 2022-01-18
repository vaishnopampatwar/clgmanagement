from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from home.models import CustomUser, Staff, Courses

def staff_home(request):
    faculties=Staff.objects.all()
    return render(request, "staff_template/staff_home_template.html",{"faculties":faculties})
