from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, parsers
from .models import  Post
from .serializers import PostSerializer

class PostViewset(viewsets.ModelViewSet):
 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']