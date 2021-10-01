from rest_framework.serializers import ModelSerializer, IntegerField
from sum.models import SumNumber
from sum.throttle import UserRateThrottle

class HistorySerializer(ModelSerializer):
    a = IntegerField(source='number1')
    b = IntegerField(source='number2')
    throttle_classes = [UserRateThrottle]
    class Meta:
        model = SumNumber
        fields = ('a', 'b')
