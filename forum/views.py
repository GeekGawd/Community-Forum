from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import viewsets, parsers
from .models import  Account, Comment, Post
from .serializers import AccountSerializer, CommentSerializer, PostSerializer

class PostViewset(generics.GenericAPIView,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AccountCreateView(generics.CreateAPIView):
    model = Account
    serializer_class = AccountSerializer

class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostLikedView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class PostLikedView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 