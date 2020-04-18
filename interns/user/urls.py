from .views import UserViewSet
from rest_framework.routers import DefaultRouter,SimpleRouter

router = SimpleRouter(trailing_slash=False)

# router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls