from django.shortcuts import render
from .shoppcart import Shoppcart
from shop.models import Product
from django.shortcuts import redirect


# Create your views here.

def add_product(request, product_id):

    shoppcart=Shoppcart(request)

    product=Product.objects.get(id=product_id)

    shoppcart.add(product=product)

    return redirect("Shop")


def delete_product(request, product_id):

    shoppcart=Shoppcart(request)

    product=Product.objects.get(id=product_id)

    shoppcart.delete(product=product)

    return redirect("Shop")


def remove_product(request, product_id):

    shoppcart=Shoppcart(request)

    product=Product.objects.get(id=product_id)

    shoppcart.remove_product(product=product)

    return redirect("Shop")


def clean_shoppcart(request, product_id):

    shoppcart=Shoppcart(request)

    shoppcart.clean_shoppcart()

    return redirect("Shop")
