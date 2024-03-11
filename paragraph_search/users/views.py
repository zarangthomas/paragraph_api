from django.shortcuts import render
from django.contrib.auth import login, get_user_model 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import views as auth_views 
from rest_framework import generics
from .serializers import UserSerializer 

User = get_user_model()

class CustomLoginView(auth_views.LoginView):
    def form_valid(self, form):
        login(self.request, form.get_user())  
        token, created = Token.objects.get_or_create(user=form.get_user())
        return Response({'token': token.key}) 

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
