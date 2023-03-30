from rest_framework import viewsets, serializers
from rest_framework.response import Response
from . import models
# Create your views here.


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = "__all__"

class StudentViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer_class = StudentSerializers(data=request.data)
        if serializer_class.is_valid():
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