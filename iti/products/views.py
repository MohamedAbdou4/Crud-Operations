from curses.ascii import HT
from itertools import product
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Product
from django.views.generic.edit import UpdateView
from .forms import ProductForm



# Create your views here.
def productsindex(request):
    allproducts = [
        {"id":1, "name":"mobile", "image":"product1.png"},
        {"id":2, "name":"laptop", "image":"product2.png"},
        {"id":3, "name":"smart tv", "image":"product3.png"},
        ]
    return  render(request, "products/allproducts.html",context={"products":allproducts})

def index(requst):
    products = Product.objects.all
    return render(requst, 'products/index.html', context={"products":products})

def show(request, id):
    product = Product.objects.get(pk=id)
    print(product.get_show_url())
    return  render(request, "products/show.html", context={"product":product})


def delete(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("/products")


def createproduct(request):

    if request.POST:
        product = Product()
        product.name = request.POST["name"]
        product.image = request.POST["image"]
        product.no_of_items = request.POST["no_of_items"]
        product.description = request.POST["description"]
        product.save()
        return redirect('/products')
    myform = ProductForm()
    return render(request, "products/create.html", context={"form":myform})

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name ='products/edit.html'
    success_url = "/products"