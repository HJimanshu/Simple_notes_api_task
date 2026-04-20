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