from rest_framework.serializers import ModelSerializer
from .models import AllProductModel

class AllProductsSerializer(ModelSerializer):
    class Meta:
        model=AllProductModel
        fields="__all__"