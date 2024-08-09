from rest_framework import serializers
from .models import Xodimlar,Davomat

class XodimlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = '__all__'

class DavomatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
