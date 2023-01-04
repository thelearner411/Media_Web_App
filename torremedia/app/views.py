from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category
from .models import Article


def helloWorld(request):
    return HttpResponse("Hello world!")

def main(request):
    categories = Category.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def browseall(request):
    categories = Category.objects.all().values()
    articles = Article.objects.all().order_by("-createdAt")

    template = loader.get_template('browseall.html')
    context = {
        'categories': categories,
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))

def browse(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all().values()
    articles = Article.objects.filter(category=id).order_by("-createdAt")

    template = loader.get_template('browse.html')
    context = {
        'category': category,
        'categories': categories,
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'categories': ['Technology', 'Health', 'Culture', 'Politics', 'Sports', 'Entertainment'],   
  }
  return HttpResponse(template.render(context, request))

def article(request, id):
    categories = Category.objects.all().values()
    article = Article.objects.get(id=id)
    template = loader.get_template('article.html')
    context = {
        'categories': categories,
        'article': article,
    }
    return HttpResponse(template.render(context, request))
