from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, parsers
from .models import  Account, Post
from .serializers import AccountSerializer, PostSerializer

class PostViewset(viewsets.ModelViewSet):
 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

class AccountCreateView(generics.CreateAPIView):
    model = Account
    serializer_class = AccountSerializer