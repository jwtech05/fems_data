from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FemsTrans
from .serializers import kwhFemsTrans_serializer
import json



class addFemsTransData1(APIView):
    def post(self, request):

        for i in range(len(request.data['payload'])):
            json_data1 = request.data['payload'][i]
            c = dict({key: value for key, value in json_data1.items() if key == 'dev_id' or key == 'dev_time'})
            d = str({key: value for key, value in json_data1.items() if key != 'dev_id' and key != 'dev_time'})
            c['payload_data'] = d
            request.data['payload'][i] = c
            request.data.update(c)
        print(request.data)
        kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)
        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)


class addFemsTransData2(APIView):
    def post(self, request):

        for i in range(len(request.data['payload'])):
            json_data1 = request.data['payload'][i]
            c = dict({key: value for key, value in json_data1.items() if key == 'dev_id' or key == 'dev_time'})
            d = str({key: value for key, value in json_data1.items() if key != 'dev_id' and key != 'dev_time'})
            c['payload_data'] = d
            request.data['payload'][i] = c
            request.data.update(c)
        del request.data['payload_data']
        print(request.data)
        kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)
        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)