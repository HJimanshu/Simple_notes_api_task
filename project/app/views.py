from django.shortcuts import render,HttpResponse
from .models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer

# Create your views here.

class Create_Note(APIView):
    # return HttpResponse("Note created successfully!")
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class NoteList(APIView):
    def get(self, request):
        queryset = Note.objects.all()
        
        #filter by is_complete
        is_complete = request.query_params.get('is_complete')
        if is_complete is not None:
            if is_complete.lower() == 'true':
                queryset = queryset.filter(is_complete=True)
            elif is_complete.lower() == 'false':
                queryset = queryset.filter(is_complete=False)
        
        #search by title
        search = request.query_params.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        #order by created_at
        ordering = request.query_params.get('ordering')
        if ordering == 'created_at':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')  # default ordering is descending by created_at         
                  
        
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)