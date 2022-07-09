# from django.shortcuts import render
from .serilaizer import TeacherSerializer,AttendanceSerializer
from .models import Teacher,Attendane
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404




@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detalis(request, id):
    teachr = get_object_or_404(Teacher, pk=id)
    
    if request.method == 'GET':
        serializer = TeacherSerializer(teachr)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teachr, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        teachr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def teacher_post(request):
    serializer = TeacherSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# class TeacherViewSet(ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


# class AttendanceViewSet(ModelViewSet):
#     queryset = Attendane.objects.all()
#     serializer_class = AttendanceSerializer

# class teacher_api(APIView):
#     def get(self,request):
#         queryset = Teacher.objects.all()
#         serializer = TeacherSerializer(queryset,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = TeacherSerializer( data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     def put(self,request):
#         serializer = TeacherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request):
#         teachr=TeacherSerializer(data=request.data)
#         teachr.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)