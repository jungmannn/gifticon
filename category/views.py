from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogDrink
# Create your views here.

def drink(request):
    drinks = BlogDrink.objects
    return render(request, 'drink.html', {'drink' : drinks })

def food(request):
    drinks = BlogDrink.objects
    return render(request, 'food.html', {'drink' : drinks })

def fashion(request):
    drinks = BlogDrink.objects
    return render(request, 'fashion.html', {'drink' : drinks })

def specialPrice(request):
    drinks = BlogDrink.objects
    return render(request, 'specialPrice.html', {'drink' : drinks })

def Drinkdetail(request, blogDrink_id):
    blogDrink_detail = get_object_or_404(BlogDrink, pk=blogDrink_id)
    return render(request, 'Drinkdetail.html', {'drink' : blogDrink_detail})