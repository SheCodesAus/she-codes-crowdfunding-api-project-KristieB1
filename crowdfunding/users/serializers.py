# users/serializers.py
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=100)
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    avatar = serializers.URLField()
    bio = serializers.CharField(max_length=1000)
    

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username'.instance.username)
        instance.firstName = validated_data.get('firstName'.instance.firstName)
        instance.lastName = validated_data.get('lastName'.instance.lastName)
        instance.avatar = validated_data.get('avatar'.instance.avatar)
        instance.bio = validated_data.get('bio'.instance.bio)
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'firstName', 'lastName')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['firstName'],
            last_name=validated_data['lastName']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user