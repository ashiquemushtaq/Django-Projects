from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import editForm

# Create your views here.

def index(request):
    obj = blog.objects.all().filter(featured=False)
    feat = blog.objects.all().filter(featured=True)
    return render(request,'index.html',{'items':obj,'feat':feat})

def login(request):
    if request.method == "POST":
        name = request.POST['your_name']
        pswd = request.POST['your_pass']
        user = auth.authenticate(username=name,password=pswd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'signin.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['email']
        pswd = request.POST['pass']
        repswd = request.POST['re_pass']
        if pswd == repswd:
            if User.objects.filter(email=mail).exists():
                messages.info(request,"Email already existing")
                return redirect('register')
            elif User.objects.filter(username=name).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=name,email=mail,password=pswd)
                user.save()
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('login')
    else:
        return render(request,'signup.html')

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        new = blog(name=name,desc=desc)
        new.save()
        return redirect('/')
    return render(request,'add.html')
def details(request,blog_id):
    b_id = blog.objects.get(id=blog_id)
    return render(request,"details.html",{'blog':b_id})

def edit(request,blog_id):
    b_id = blog.objects.get(id=blog_id)
    form = editForm(request.POST or None,instance=b_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form})

def delete(request,blog_id):
    b_id = blog.objects.get(id=blog_id)
    if request.method == 'POST':
        b_id.delete()
        return redirect('/')
    return render(request,'done.html')
def logout(request):
    auth.logout(request)
    return redirect('login')