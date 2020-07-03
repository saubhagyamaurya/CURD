from rest_framework import serializers
from .models import Users,update,delete,single


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class updateSerializer(serializers.ModelSerializer):
  class Meta:
    model = update
    fields = '__all__'

class deleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = delete
        fields = '__all__'

class singleSerializer(serializers.ModelSerializer):
    class Meta:
        model = single
        fields = '__all__'
