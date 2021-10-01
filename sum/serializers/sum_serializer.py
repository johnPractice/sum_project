from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from sum.models import SumNumber


class SumSerializer(ModelSerializer):

    class Meta:
        model = SumNumber
        fields = '__all__'

    @property
    def data(self):
        ret = super().data
        result = ret['number1']+ret['number2']
        return {'result': result}
