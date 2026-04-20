from symtable import Class

from django.contrib import admin
from .models import Note
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_complete')
    list_filter = ('is_complete')
admin.site.register(Note, NoteAdmin)