from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Landing(request):
    return render(request,'Main/index.html')