from rest_framework.generics import ListAPIView
from sum.models import SumNumber
from sum.serializers.history_serializer import HistorySerializer
from rest_framework.throttling import UserRateThrottle
from utils import OneHunderdPage


class HistoryView(ListAPIView):

    serializer_class = HistorySerializer
    pagination_class = OneHunderdPage
    queryset = SumNumber.objects.all()
    throttle_classes = [UserRateThrottle]
