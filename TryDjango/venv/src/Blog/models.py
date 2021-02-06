from django.db import models
import datetime
from datetime import date
from django.urls import reverse

# Create your models here.
class Article (models.Model):
  title = models.CharField(max_length=50) #title
  body = models.TextField()
  author = models.CharField(max_length=50) #default=request.user #title
  date = models.DateField(blank=True, null=True) #date  

def get_absolute_url (self):
  return reverse("Blog:article-detail", kwargs={"id": self.id})
