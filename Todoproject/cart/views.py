from django.shortcuts import render,redirect
from TodoApp.models import Product
from.models import Cart
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def addcart(req,id):
    user=req.session['user']
    Product=Product.objects.get(id=id)
    print(product)
    try:
        cart=Cart.objects.get(product=product)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoseNotExist:
        cart=Cart.objects        
            
