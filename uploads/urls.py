from django.urls import path
from . import views

urlpatterns = [
    path('upload/files/' , views.upload_sales)
]