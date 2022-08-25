from rest_framework.routers import SimpleRouter
from .views import PostViewset
router = SimpleRouter()
router.register('accounts', PostViewset)
urlpatterns = router.urls