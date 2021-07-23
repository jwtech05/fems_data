from rest_framework import serializers
from .models import FemsTrans,FemsPayload


class kwhFemsPayload(serializers.ModelSerializer):
    class Meta:
        model = FemsPayload
        fields =  ('dev_id','dev_time','payload_data')

class kwhFemsTrans_serializer(serializers.ModelSerializer):
    payload = kwhFemsPayload(many=True)

    class Meta:
        model = FemsTrans
        fields = ('transaction_id', 'site_id', 'eng_type', 'version', 'payload','dev_id', 'dev_time')

    def create(self, validated_data):
        payload_data = validated_data.pop('payload')
        site = FemsTrans.objects.create(**validated_data)
        for payloads_data in payload_data:
            FemsPayload.objects.create(site=site, **payloads_data)
        return site


