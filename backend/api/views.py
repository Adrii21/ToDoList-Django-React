from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class CreateNoteList(generics.ListCreateAPIView):

    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)     #.all() para devolverlo todo (posible mejora para añadir a admin)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)   # On serializers.py we set the author with extra kwargs as read_only
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
#    def perform_delete(self, serializer):
#        if serializer.is_valid():
 #           serializer.
        


class CreateUserView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]