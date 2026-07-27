from rest_framework.routers import DefaultRouter
from .views import HotelDetailsViewSet

router = DefaultRouter()
router.register(r'hotelDetails', HotelDetailsViewSet)

urlpatterns = router.urls