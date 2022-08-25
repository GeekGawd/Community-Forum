from rest_framework.routers import SimpleRouter
from .views import PostViewset
from django.urls import path
from .views import *

router = SimpleRouter()

router.register('post', PostViewset)
urlpatterns = router.urls

urlpatterns = [
    path('register/', AccountCreateView.as_view()),
]