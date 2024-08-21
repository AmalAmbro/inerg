from rest_framework.serializers import ModelSerializer

from core.models import Well

class WellSerializer(ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'
