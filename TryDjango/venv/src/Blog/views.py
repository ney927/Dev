from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import get_absolute_url

# Create your views here.

def article_list_view(request):
  queryset = Article.objects.all()
  context={
    'obj_list': queryset
  }
  return render(request, 'Blog/article_list.html', context)

def article_detail_view(request, id):
  obj = get_object_or_404(Article, id=id)
  obj = Article.objects.get(id=id)
  context = {
    'obj': obj
  }
  return render(request, 'Blog/article_detail.html', context)