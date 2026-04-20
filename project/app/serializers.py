from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'is_complete']
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value  
    
    
    
    
    
