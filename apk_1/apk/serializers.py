from rest_framework import serializers
from . models import Register , Login

class RegisterSerializer(serializers.Serializer):
    f_name =  serializers.CharField(max_length=50)
    l_name =  serializers.CharField(max_length=50)
    Phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    pass_1 = serializers.CharField(max_length=256)
    City = serializers.CharField(max_length=50)
    State = serializers.CharField(max_length=50)
    Country = serializers.CharField(max_length=20)
    Zip_code = serializers.IntegerField()

    def create(self,validate_data):
        return Register.objects.create(**validate_data)

class LoginSerializer(serializers.Serializer):
    Email = serializers.EmailField()
    pass_1 = serializers.CharField(max_length=256)
    
    def create(self, validated_data):
        return Login.objects.create(**validated_data)