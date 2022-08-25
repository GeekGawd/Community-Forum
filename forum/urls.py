from rest_framework.routers import SimpleRouter
from .views import PostViewset

router = SimpleRouter()

router.register('post', PostViewset)
urlpatterns = router.urls