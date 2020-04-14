from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from .models import Cart
from product.models import Product
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def viewcart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id=None
    if the_id:
        cart_queryset = Cart.objects.get(id=the_id)
    else:
        cart_queryset = None
    return render(request, 'cart/listview.html', {"cart_queryset":cart_queryset})

def updatecart(request, pk):
    request.session.set_expiry(3)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    try:
        prod = Product.objects.get(pk=pk)
    except:
        pass
    if not prod in cart.product.all():
        cart.product.add(prod)
    else:
        cart.product.remove(prod)
    my_total = 0.00
    for i in cart.product.all():
        my_total += i.price
    print(my_total)
    cart.total = my_total
    cart.save()
    return HttpResponseRedirect(reverse("cart:viewcart"))    