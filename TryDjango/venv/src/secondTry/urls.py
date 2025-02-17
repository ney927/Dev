"""secondTry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import include, path
from pages.views import contact_view, home_view, deleteDoc_view
from Products.views import product_detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('Products.urls')),
    path('article/', include('Blog.urls')),
    path('tasks/', include('ToDo.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='products'),
    path('document/<int:pk>/', deleteDoc_view, name='delete-doc'),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
