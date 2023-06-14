from rest_framework import serializers
from Doctor.models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Organization


def usernameAlreadyExist(username):
    return User.objects.filter(username=username).exists()
def emailAlreadyExist(email):
    return User.objects.filter(email=email).exists()

class CreateDoctorSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    def validate(self, attrs):

        username = attrs.get('username')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        email = attrs.get('email')

        if password != confirm_password:
            raise serializers.ValidationError({'error' : 'password does not matching with password confermation'})
        if password == None:
            raise serializers.ValidationError({'error' : 'password must be set'})
        if username == None:
            raise serializers.ValidationError({'error' : 'username must be set'})
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        if usernameAlreadyExist(username):
            raise serializers.ValidationError({'error' : 'username already exist try again'})
        if emailAlreadyExist(email):
            raise serializers.ValidationError({'error' : 'email already exist'})

        return attrs
    
    def create(self, validated_data):
        user = self.context['request'].user
        username = validated_data.get('username')
        password = validated_data.get('password')
        email    = validated_data.get('email')
        try:
            org = Organization.objects.get(user = user)
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        try:
            user = User(
                username = username,
                email = email,
                password = password
            )
            user.save()
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        try:
            doctor = Doctor(
                user = user,
                organization = org
            )
            doctor.save()
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        return user
    
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

        
class DeleteDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    def delete(self):
        instance = self.instance
        instance.delete()