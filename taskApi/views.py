from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import task
from .serializers import taskSerializer


class taskList(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            query = task.objects.get(pk=id)
            serializer = taskSerializer(query)
            return Response(serializer.data)
        else:
            query = task.objects.all()
            serializer = taskSerializer(query, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'task created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def put(self, request, pk=None, format=None):
        id = pk
        query = task.objects.get(pk=id)
        serializer = taskSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'task details updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'employe details updation failed'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        query = task.objects.get(pk=id)
        query.delete()
        return Response({'msg': 'task deleted successfully'})
