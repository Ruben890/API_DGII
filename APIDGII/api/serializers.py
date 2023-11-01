from rest_framework  import serializers
from ..models import RNC

class RNC_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RNC
        fields = "__all__"
        