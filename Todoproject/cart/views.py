from django.shortcuts import render,redirect
from TodoApp.models import Product
from.models import Cart
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    try:
        cart=Cart.objects.get(product=product)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
    except Cart.DoseNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)
    return redirect('cart:displaycart')


def displaycart(req):
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user) 
    return render(req,'cart.html',{'cart':cart})      