from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django admin panel
    path('', index, name='index'),  # URL for the home page
    path('update_task/<int:pk>/', update_item, name='update_task'),  # URL for updating a task
    path('delete_task/<int:pk>/', delete_item, name='delete_task'),  # URL for deleting a task
    path('finished/<int:pk>/', finished, name='finished'),  # URL for marking a task as finished
]
