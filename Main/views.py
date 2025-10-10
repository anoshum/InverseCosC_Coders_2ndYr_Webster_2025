from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Complain,Usr,Worker
from django.contrib import messages
    
import datetime

# Create your views here.
def Landing(request):
    complains = Complain.objects.all()
    return render(request,'Main/index.html',{'complains':complains})
    
def File_new(request):
    un = request.POST['un']
    return render(request,'Main/file_complain.html',{'usern':un})
def F_n(request):
    un = request.POST['un']
    cat = request.POST['cat']
    desc = request.POST['desc']
    lm = request.POST['lm']
    lat = request.POST['lat']
    long = request.POST['long']
    imge = request.FILES['image']
    complain = Complain(domain_name = cat,
    user_name = un,
    status = 'Pending',
    info = desc,
    landmark = lm,
    image = imge,
    locx = lat,
    locy = long,
    datee = datetime.datetime.now())
    complain.save()
    messages.info(request,'filed')
    return render(request,'Main/user_dash.html',{'usern':un,'filed':True})
     


def Sign_Up(request):
    if request.method == 'POST':
        fulln = request.POST['fn']
        numb = request.POST['num']
        usern = request.POST['un']
        email = request.POST['em']
        pass_w = request.POST['ps']
        user = Usr(real_name=fulln,user_name = usern,user_pass = pass_w,user_phone = numb,user_email = email,user_complains = 0)
        user.save()
        messages.info(request,'Done, Now you can Sign in')
        return redirect('/')
    else:
        return render(request,'Main/signup.html')


def Dash(request):
    un = request.POST['un']
    ps = request.POST['ps']
    
    complains = Complain.objects.filter(user_name = un)
    return render(request,'Main/user_dash.html',{'complains':complains,'usern':un})
def admin_page(request):
    complains = Complain.objects.all()
    return render(request,'Main/admin_page.html',{'complains':complains}) 
def worker(request):
    return render(request,'Main/worker_page.html')