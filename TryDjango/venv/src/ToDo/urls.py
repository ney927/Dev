from django.urls import path
from .views import (
  tasks_list_view,
  tasks_create_view,
  tasks_delete_view,
  tasks_complete_view,
)

appname = 'ToDo'
urlpatterns = [
  path('list/', tasks_list_view, name='tasks-list'),
  path('create/', tasks_create_view, name='tasks-create'),
  path('delete/<int:id>', tasks_delete_view, name='tasks-delete'),
  path('complete/<int:id>', tasks_complete_view, name='tasks-complete'),
] 