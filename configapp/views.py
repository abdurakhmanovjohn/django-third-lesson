from django.shortcuts import render
# from django.http import HttpResponse
from .models import *


def index(request):
  news = News.objects.all()
  categories = Categories.objects.all()
  context = {
    'news': news,
    'categories': categories,
    'title': "The Title"
  }
  return render(request, 'index.html', context)


