from rest_framework import serializers
from .models import FemsTrans,FemsPayload


class kwhFemsPayload(serializers.ModelSerializer):
    # dev = serializers.CharField(required=True)
    # dev_time = serializers.CharField(required=True)
    payload_data = serializers.ListField()
    class Meta:
        model = FemsPayload
        fields =  ('dev','dev_time','payload_data')
class kwhFemsTrans_serializer(serializers.ModelSerializer):

    payload = kwhFemsPayload(many=True)

    class Meta:
        model = FemsTrans
        fields = ('transaction_id', 'site_id', 'eng_type', 'version','payload')