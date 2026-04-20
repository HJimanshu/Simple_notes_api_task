from django.contrib import admin
from django.urls import path
from .views import Create_Note

urlpatterns = [
    path('create_note/', Create_Note.as_view(), name='create_note'),
]
