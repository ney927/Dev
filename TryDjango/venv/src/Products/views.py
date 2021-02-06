from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.

def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
  context={
    'form': form
  }
  return render(request, 'Products/product_create.html', context)

# def product_create_view(request):
#   print(request.GET['title'])
#   print(request.POST)
#   my_title = request.POST.get('title')
#   print(my_title)
#   # Product.objects.create(title=my_title)
#   context={}
#   return render(request, 'product_create.html', context) 

# def product_create_view(request): 
#   my_form = RawProductForm()
#   if request.method == 'POST':
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context={
#     "form": my_form
#   } 
#   return render(request, 'product_create.html', context) 

def product_detail_view(request):
  obj = Product.objects.get(id=1)
  context={
    # 'title': obj.title,
    # 'price': obj.price,
    # 'summary': obj.summary,
    # 'featured': obj.featured
    'object': obj
    }
  return render(request, 'Products/detail.html', context) 

def dynamic_lookup_view(request, id):
  # obj = get_object_or_404(Product, id=id)
  # obj = Product.objects.get(id=id)
  try:
    obj = Product.objects.get(id=id)
  except Product.DoesNotExist:
    raise Http404
  context={
    'object': obj
    }
  return render(request, 'Products/detail.html', context) 

def product_delete_view(request, id):
  obj = get_object_or_404(Product, id=id)
  # if request.method == 'POST':
  #   # confirming delete
  #   obj.delete()
  queryset = Product.objects.all()
  context={
    'object_list': queryset
    }
  return render(request, 'Products/product_delete.html', context)

def render_view(request):
  initial_data = {
    'title': "My Awesome Title"
  } 
  obj = Product.objects.get(id=1)
  form = RawProductForm(request.POST or None, initial=initial_data, instance=obj)
  context={ 
    'form': form
  } 
  return render(request, 'Products/product_create.html', context) 