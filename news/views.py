from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    content = {
        'news':news,
        'title': "World News",
        'categories': categories
    }
    return render(request,'news/index.html', context=content)


def get_cat(req,cat_id):
    news = News.objects.filter(category_id= cat_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=cat_id)
    return render(req,'news/category.html',{'news':news,'category':category,'categories':categories})