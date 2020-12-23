from rest_framework import serializers
from backend.models import Taskinfo 
from django.contrib.auth.models import User

class TaskinfoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Taskinfo
        fields  = ('id','task','status','created','user')

class UserSerializier(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Taskinfo.objects.all())
    class Meta:
        model = User
        fields = ('id','username','tasks')
        

   