from django.shortcuts import render
from django.http.response import HttpResponse
from curdapp.forms import Productupdateform, Productdeleteform
from .models import ProductData
from .forms import ProductForm
# Create your views here.
def main_page(request):
    return render(request,'main_page.html')
def product_insert_view(request):
    if request.method=="POST":
        iform=ProductForm(request.POST)
        if iform.is_valid():
            product_id=request.POST.get('product_id')
            product_name=request.POST.get('product_name')
            product_cost=request.POST.get('product_cost')
            product_color=request.POST.get('product_color')
            product_class=request.POST.get('product_class')
            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_color=product_color,
                product_class=product_class
            )
            data.save()
            iform=ProductForm()
            return render(request,'insert.html',{'iform':iform})

    else:
        iform=ProductForm()
        return render(request,'insert.html',{'iform':iform})
def product_retrieve(request):
    products=ProductData.objects.all()
    return render(request,'retrieve.html',{'products':products})
def product_update(request):
    if request.method=="POST":
        uform=Productupdateform(request.POST)
        if uform.is_valid():
            product_id=request.POST.get('product_id')
            product_cost=request.POST.get('product_cost')
            pid=ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse("Product is Not available")
            else:
                pid.update(product_cost=product_cost)
                uform=Productupdateform()
                return render(request,'update.html',{'uform':uform})

        else:
            return HttpResponse("user invalid data")
    else:
        uform=Productupdateform()
        return render(request,'update.html',{'uform':uform})
def product_delete_view(request):
    if request.method=="POST":
        dform=Productdeleteform(request.POST)
        if dform.is_valid():
            product_id=request.POST.get('product_id')
            pid=ProductData.objects.filter(product_id=product_id)
            if not pid:
                return HttpResponse("Product is Not Available")
            else:
                pid.delete()
                dform=Productdeleteform()
                return render(request,'delete.html',{'dform':dform})
    else:
        dform=Productdeleteform()
        return render(request,'delete.html',{'dform':dform})