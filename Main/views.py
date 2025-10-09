from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'Main/admin_page.html') 
def worker(request):
    return render(request,'Main/worker_page.html')