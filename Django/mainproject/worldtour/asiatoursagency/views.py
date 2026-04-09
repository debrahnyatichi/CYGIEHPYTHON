from django.shortcuts import render
from .models import Tour


# Create your views here.
def index(request):
    return render(request, 'tours/index.html')