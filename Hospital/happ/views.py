from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import doctor,department,patient
# Create your views here.
def index(request):
    dctr = doctor.objects.all().filter(featured=True)
    dpt = department.objects.all()
    return render(request,'index.html',{'doctor':dctr,'depart':dpt})

def about(request):
    dpt = department.objects.all()
    return render(request,'about.html',{'depart':dpt})

def appointment(request):
    dctr = doctor.objects.all()
    dpt = department.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        phn = request.POST['mobile']
        mail = request.POST['mail']
        depart = request.POST['department']
        doc = request.POST['doctor']
        pat = patient(name=name,email=mail,phone=phn,doctor=doc,department=depart)
        pat.save()
        return redirect('/')
    return render(request,'appointment.html',{'depart':dpt,'doctor':dctr})

def doctors(request):
    dpt = department.objects.all()
    dctr = doctor.objects.all()
    return render(request,'doctors.html',{'doctor':dctr,'depart':dpt})

def departments(request,dep_slug=None):
    dpt = department.objects.all()
    doct = None
    # dep_slug = department.objects.get(slug=dep_slug)
    if dep_slug!= None:
        dep_page = get_object_or_404(department,slug=dep_slug)
        doct = doctor.objects.filter(dep=dep_page)
        if len(doct)<1:
            messages.info(request,"No Doctors available")
    return render(request,'department.html',{'depart':dpt,'doctor':doct})