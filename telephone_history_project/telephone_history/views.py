from rest_framework import generics
from .models import TelephoneHistory
from .serializers import TelephoneHistorySerializer

class TelephoneHistoryList(generics.ListAPIView):
    queryset = TelephoneHistory.objects.all()
    serializer_class = TelephoneHistorySerializer
