from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from . import models
from threading import Thread
# Create your views here.


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = "__all__"


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class StudentViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer_class = StudentSerializers(data=request.data)
        if serializer_class.is_valid():
            # consumer_thread = Thread(target=consume_records)
            # consumer_thread.start()
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.error_messages)
     
    
    def list(self, request):
        res = models.StudentModel.objects.all()
        serializer_class = StudentSerializers(res, many= True)
        return Response(serializer_class.data)
    

    def retrieve(self, request, pk=None):
        try:
            res = models.StudentModel.objects.get(pk=pk)
            serializer_class = StudentSerializers(res)
            return Response(serializer_class.data)
        except Exception:
            return Response({"status": "404"})