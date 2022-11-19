from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
# Create your views here.
def index(request):
    for prod in Product.objects.all():
        print(prod.desc)
    # print(Product.objects.all())
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return render(request,'product.html')
def about(request):
    print('render run')
    return render(request,'about.html')
def search(request):
    return render(request,'search.html')
def checkout(request):
    return render(request,'checkout.html')
def tracker(request):
    return render(request,'tracker.html')