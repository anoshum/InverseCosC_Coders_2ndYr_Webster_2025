from django.shortcuts import render
from django.http import HttpResponse
from .models import Complain
# Create your views here.
def Landing(request):
    return render(request,'Main/index.html')
def File_new(request):
    return render(request,'Main/file_complain.html')
def Sign_Up(request):
    return render(request,'Main/signup.html')
def Dash(request):
    return render(request,'Main/user_dash.html')
def admin_page(request):
    complains = Complain.objects.all()
    return render(request,'Main/admin_page.html',{'complains':complains}) 
def worker(request):
    return render(request,'Main/worker_page.html')