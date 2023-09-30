from django.shortcuts import render
from django.http import HttpResponse
from .models import config_collection

def index(request, *args, **kwargs):
    config = config_collection.find_one()
    return HttpResponse(f"<h1>Hello {str(config['Hello'])}</h1>")
