from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..serializers import *
from ..models import *

def home(request):
    return render(request,'client/pages/home.html')

