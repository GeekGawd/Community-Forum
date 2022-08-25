from rest_framework.routers import SimpleRouter
from .views import PostViewset
from django.urls import path
from .views import *

urlpatterns = [
    path('post/', PostViewset.as_view()),
    path('register/', AccountCreateView.as_view()),
]