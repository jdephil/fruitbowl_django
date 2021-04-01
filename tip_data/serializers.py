from rest_framework import serializers
from tip_data.models import Tip

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ('title', 'category', 'url', 'urlTitle')