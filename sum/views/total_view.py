from rest_framework.views import APIView
from sum.models import SumNumber
from rest_framework.response import Response
from sum.throttle import UserRateThrottle


class TotalView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request,  format=None):
        return Response(data=SumNumber.get_total_vlaue())
