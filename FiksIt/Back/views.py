from django.shortcuts import render

# Create your views here.
def admin_page(request):
    return render(request,'Back/admin_page.html') 
def worker(request):
    return render(request,'Back/worker_page.html')