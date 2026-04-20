from django.contrib import admin
from django.urls import path
from .views import Create_Note,NoteList

urlpatterns = [
    path('create_note/', Create_Note.as_view(), name='create_note'),
    path('notes/', NoteList.as_view(), name='note_list'),
]


