from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404

from product.models import Product
from product.forms import ProductForm
# Create your views here.

def productlist(request):
    product_queryset = Product.objects.all()
    return render(request, 'product/listview.html', {"product_queryset":product_queryset})

def createproduct(request):
    product_form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product:productlist'))
    return render(request, 'product/createview.html', {"form":product_form})

def deleteview(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('product:productlist')) 
