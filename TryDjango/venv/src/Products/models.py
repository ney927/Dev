from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  summary = models.TextField(default='yeayea')
  featured = models.BooleanField(default=True)

  def get_absolute_url(self):
    return reverse("Products:products", kwargs={"id": self.id})
    #return f"/products/{self.id}/"