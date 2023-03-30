from django.http import JsonResponse, Http404
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from threading import Thread
import time
# Create your views here.


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = "__all__"


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class StudentViewSet(viewsets.ViewSet):

    def create(self, request):
        lastTime = request.session.get('last_request_time')
        if lastTime is not None:
            elapseTime = time.time() - lastTime
            time_remaining = 60 - elapseTime
            print(type(time_remaining))
            print(time_remaining)
            if int(time_remaining) > 0:
                return JsonResponse({"status": f"Please wait for {time_remaining:.2f} seconds"})
            
        request.session['last_request_time'] = time.time()
        serializer_class = StudentSerializers(data=request.data)
        if serializer_class.is_valid():
            # consumer_thread = Thread(target=consume_records)
            # consumer_thread.start()
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.error_messages)
     
    
    def list(self, request):
        
        lastTime = request.session.get('last_request_time')
        if lastTime is not None:
            elapseTime = time.time() - lastTime
            time_remaining = 60 - elapseTime
            print(type(time_remaining))
            print(time_remaining)
            if int(time_remaining) > 0:
                return JsonResponse({"status": f"Please wait for {time_remaining:.2f} seconds"})
            
        request.session['last_request_time'] = time.time()

        res = models.StudentModel.objects.all()
        serializer_class = StudentSerializers(res, many= True)
        return Response(serializer_class.data)
    

    def retrieve(self, request, pk=None):
        lastTime = request.session.get('last_request_time')
        if lastTime is not None:
            elapseTime = time.time() - lastTime
            time_remaining = 60 - elapseTime
            print(type(time_remaining))
            print(time_remaining)
            if int(time_remaining) > 0:
                return JsonResponse({"status": f"Please wait for {time_remaining:.2f} seconds"})
            
        request.session['last_request_time'] = time.time()
        try:
            res = models.StudentModel.objects.get(pk=pk)
            serializer_class = StudentSerializers(res)
            return Response(serializer_class.data)
        except Exception:
            return JsonResponse({"status": "404"})