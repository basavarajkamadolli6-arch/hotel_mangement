from rest_framework import viewsets
from .models import HotelDetails
from .serializers import HotelDetailsSerializer

class HotelDetailsViewSet(viewsets.ModelViewSet):
    queryset = HotelDetails.objects.all()
    serializer_class = HotelDetailsSerializer