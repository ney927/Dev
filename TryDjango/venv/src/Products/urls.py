from django.urls import path
from .views import (
  product_detail_view, 
  product_create_view, 
  render_view, 
  dynamic_lookup_view, 
  product_delete_view,
)

app_name = 'Products'
urlpatterns = [
  # path('Products/detail/', product_detail_view, name='detail'), 
  path('create/', product_create_view, name='create'),
  path('render/', render_view, name='render'),
  path('<int:id>/', dynamic_lookup_view, name='products'),
  path('<int:id>/delete/', product_delete_view, name='products-delete'),
]