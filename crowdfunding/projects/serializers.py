# from unittest.util import _MAX_LENGTH
# from msilib.schema import _Validation_records
from unicodedata import category
from rest_framework import serializers
from .models import Project, Pledge, Category, PledgeType

class PledgeTypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pledge_type_name = serializers.ReadOnlyField()
    pledge_id = serializers.IntegerField()

    def create(self, validated_data):
        return PledgeType.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    pledge_type = PledgeTypeSerializer(many=True, read_only=False)

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project_id = serializers.IntegerField()
    category_name = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    blurb = serializers.CharField(max_length=200)
    category = CategorySerializer(many=True, read_only=False)
    goal = serializers.IntegerField()
    goal_date = serializers.DateTimeField()
    progress = serializers.IntegerField()
    primary_image = serializers.URLField()
    status = serializers.CharField(max_length=200)
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # category = serializers.IntegerField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    description = serializers.CharField(max_length=200)
    secondary_image = serializers.URLField()
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.goal_date = validated_data.get('goal_date', instance.goal_date)
        instance.progress = validated_data.get('progress', instance.progress)
        instance.status = validated_data.get('status', instance.status)
        instance.primary_image = validated_data.get('primary_image', instance.primary_image)
        instance.secondary_image = validated_data.get('secondary_image', instance.secondary_image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance