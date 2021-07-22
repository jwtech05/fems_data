from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FemsTrans
from .serializers import kwhFemsTrans_serializer
import json



class addFemsTransData(APIView):
    def post(self, request):
        kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)

        for i in range(len(request.data['payload'])):
            json_data1 = request.data['payload'][i]
            c = dict({key: value for key, value in json_data1.items() if key == 'dev_id' or key == 'dev_time'})
            d = str({key: value for key, value in json_data1.items() if key != 'dev_id' and key != 'dev_time'})
            c['payload_data'] = d
            request.data['payload'][i] = c
        print(request.data)
        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(kwhFemsTrans.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)

