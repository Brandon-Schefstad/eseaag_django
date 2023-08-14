from django.shortcuts import render
from django.http import HttpResponse

from .models import Accommodation
# Create your views here.
def accommodations(request):
    accommodations = Accommodation.objects.all()
    return render(request, 'accommodations.html', {"accommodations":accommodations})