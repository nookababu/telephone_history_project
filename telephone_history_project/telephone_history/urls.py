from django.urls import path
from .views import TelephoneHistoryList

urlpatterns = [
    path('api/telephone-history/', TelephoneHistoryList.as_view(), name='telephone_history_api'),
]
