from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document

# Create your views here.
# request.user
def home_view(request, *args,**kwargs):
  #return HttpResponse("<h1>Home Page<h1/>")
  my_context = {
    "text": "birthday is", 
    "date": "9/27/04", 
    "list": ['ok', 'yeah', 'i mean', 'shore'], 
    "truthing": True
  } 
  return render(request, 'home.html', my_context)

def deleteDoc_view(request, pk):
  if request.method == 'POST':
    obj = Document.objects.get(pk=pk)
    print(obj.doc)
    obj.delete()
  return redirect('products')

def contact_view(request, *args, **kwargs):

  form = DocumentForm()
  if request.method=='POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid:
      form.save()
      return redirect('products')
  else:
    form = DocumentForm()

  Docs = Document.objects.all()
  context={
    'form': form,
    'Document_list': Docs,
  }

  if request.method == 'POST':
    uploaded_file = request.FILES['document']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    Da_url = fs.url(name)
    print(Da_url)
    context={
      'url': Da_url 
    }
  
  return render(request, 'contact.html', context)


