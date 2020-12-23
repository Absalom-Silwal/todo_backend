from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Taskinfo
from backend.serializers import TaskinfoSerializer,UserSerializier
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from backend.permissions import  IsOwner
# Create your views here.

'''class Tasklist(APIView):
    def get(self,request,format=None):
        tasks = Taskinfo.objects.all()
        serializier=TaskinfoSerializer(tasks,many=True)
        return Response(serializier.data)
    def post(self,request,format=None):
        serializier=TaskinfoSerializer(data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data)
        return Response(serializier.errors)

class TaskDetail(APIView):
    def get_objects(self,task_id):
        try:
            return Taskinfo.objects.get(pk=task_id)
        except Taskinfo.DoesNotExist:
            raise Http404
    def get(self,request,task_id,format=None):
        task = self.get_objects(task_id)
        serializer = TaskinfoSerializer(task)
        return Response(serializer.data)
    
    def post(self,request,task_id,format=None):
        task = self.get_objects(task_id)
        serializer = TaskinfoSerializer(task,request.data)
        if serializer.is_vaid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,task_id,format=None):
        task = self.get_objects(task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


class Tasklist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = TaskinfoSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Taskinfo.objects.filter(user=user)
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user) #save the task along with its creator
         
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    queryset = Taskinfo.objects.all()
    serializer_class = TaskinfoSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializier

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializier