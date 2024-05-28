from django.shortcuts import render
from .models import category,subcategory 
# Create your views here.

def Index(request):
    category_list = category.objects.all()
    return render(request,'index.html',context = {
        'category_list':category_list,
    })
    
