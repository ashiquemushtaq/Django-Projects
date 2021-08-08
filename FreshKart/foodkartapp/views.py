from django.shortcuts import render,get_object_or_404
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

def index(request,c_slug=None):
    c_page = None
    prod = None
    if c_slug!= None:
        c_page = get_object_or_404(category,slug=c_slug)
        prod = product.objects.filter(category=c_page)
    else:
        prod = product.objects.all()
    cat = category.objects.all()
    return render(request,'index.html',{'product':prod,'category':cat})

def details(request,c_slug,p_slug):
    try:
        prodt = product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'details.html',{'prod':prodt})

def cart(request,tot=0,count=0,cart_items=None):
    ct_items = None
    try:
        ct = cartlist.objects.get(cart_id=cart_id(request))
        ct_items = items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prod.price*i.quant)
            count += i.quant
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'c_items':ct_items,'t':tot})

def cart_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=cart_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=cart_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prod=prod,cart=ct)
        if c_items.quant < c_items.prod.stock:
            c_items.quant += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(prod=prod, quant=1, cart=ct)
        c_items.save()
    return redirect('cart')
def min_cart(request,product_id):
    ct = cartlist.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(product,id=product_id)
    c_items = items.objects.get(prod=prod,cart=ct)
    if c_items.quant > 1:
        c_items.quant-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')
def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prod=prod, cart=ct)
    c_items.delete()
    return redirect('cart')