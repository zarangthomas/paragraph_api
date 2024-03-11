# search/views.py
from django.shortcuts import render
from django.contrib.auth import login 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import views as auth_views 
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Paragraph, word_index  
from .serializers import ParagraphSerializer 
from .serializers import ParagraphSerializer 

class CustomLoginView(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())  
        token, created = Token.objects.get_or_create(user=form.get_user())
        return Response({'token': token.key}) 

class ParagraphCreateView(generics.CreateAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

class ParagraphListView(generics.ListAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) 

class ParagraphSearchView(generics.ListAPIView):
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.GET.get('q') 
        if search_term:
            matching_paragraph_ids = word_index.get(search_term, [])
            return Paragraph.objects.filter(id__in=matching_paragraph_ids)
        else:
            return Paragraph.objects.none()