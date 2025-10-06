from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Landing(request):
    return render(request,'Main/index.html')
def File_new(request):
    return render(request,'Main/file_complain.html')
def Sign_Up(request):
    return render(request,'Main/signup.html')
