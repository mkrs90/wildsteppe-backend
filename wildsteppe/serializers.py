from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    # username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name']

class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = ['id', 'name']

class TrailWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'name', 'location', 'description', 'distance', 'duration', 'image', 'pets_allowed', 'difficulty']


class TrailSerializer(serializers.ModelSerializer):
    difficulty = DifficultySerializer()
    class Meta:
        model = Trail
        fields = ['id', 'name', 'location', 'description', 'distance', 'duration', 'image', 'pets_allowed', 'difficulty']

