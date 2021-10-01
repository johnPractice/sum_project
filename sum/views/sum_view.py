from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from sum.serializers import SumSerializer
from utils.global_error import BadRequestInput
from rest_framework.permissions import AllowAny

class SumView(APIView):
    permission_classes=(AllowAny,)
    def get(self, request):
        number1 = request.query_params.get('a')
        number2 = request.query_params.get('b')
        if not number1 or not number2:
            raise BadRequestInput()
        # TODO"
        total_number = int(number1)+int(number2)
        data = {'number1': number1, 'number2': number2,
                'total_number': total_number}

        sum_serializer = SumSerializer(data=data)
        sum_serializer.is_valid(raise_exception=True)
        sum_serializer.save()

        return Response(data=sum_serializer.data, status=status.HTTP_200_OK)
