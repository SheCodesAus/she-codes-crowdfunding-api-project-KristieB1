# from unittest.util import _MAX_LENGTH
# from msilib.schema import _Validation_records
from unicodedata import category
from django.forms import ValidationError
from rest_framework import serializers
from django.db.models import Sum
from .models import Project, Pledge, Category, PledgeType

class PledgeTypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    pledge_type_name = serializers.CharField(max_length=200)
    

    def create(self, validated_data):
        return PledgeType.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()
    # pledge_type_id = serializers.IntegerField()
    pledge_type = serializers.ReadOnlyField(source='project.pledge_type.pledge_type_name')
    supporter = serializers.ReadOnlyField(source='supporter.id')
    supporter_name = serializers.ReadOnlyField(source='supporter.username')

    def create(self, validated_data):
        # print(**validated_data)
        return Pledge.objects.create(**validated_data)
        

class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    category_name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    blurb = serializers.CharField(max_length=200)
    category_id = serializers.IntegerField()
    goal = serializers.IntegerField()
    goal_date = serializers.DateTimeField()
    # progress = serializers.IntegerField()
    primary_image = serializers.URLField()
    status = serializers.CharField(max_length=200)
    is_open = serializers.BooleanField()
    date_created = serializers.ReadOnlyField()
    pledge_type_id = serializers.IntegerField()
    total_pledged = serializers.SerializerMethodField()
    progress_perc = serializers.SerializerMethodField()

    def get_total_pledged(self, obj):
        return Project.objects.filter(pk=obj.id).annotate(
            total_pledged=Sum('pledges__amount')
        )[0].total_pledged

    def get_progress_perc(self, obj):
        total_pledged = Project.objects.filter(pk=obj.id).annotate(
            total_pledged=Sum('pledges__amount')
        )[0].total_pledged
        if total_pledged:
            return (total_pledged/obj.goal)*100
        else:
            return 0
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_name = serializers.ReadOnlyField(source='owner.username')
    # def validate_goal_date(self, obj):
     
    #     if obj.goal_date==obj.date_created:
    #         raise serializers.ValidationError("Your Goal Date must be in the future")
    #     return goal_date
    

    # category = serializers.IntegerField()
    # owner = serializers.CharField(max_length=200)
    # owner = serializers.ReadOnlyField(source='owner.id')
    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    description = serializers.CharField(max_length=200)
    secondary_image = serializers.URLField()
    pledges = PledgeSerializer(many=True, read_only=True)
    pledge_type = serializers.ReadOnlyField(source='pledge_type.pledge_type_name')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.goal_date = validated_data.get('goal_date', instance.goal_date)
        # instance.progress = validated_data.get('progress', instance.progress)
        instance.status = validated_data.get('status', instance.status)
        instance.primary_image = validated_data.get('primary_image', instance.primary_image)
        instance.secondary_image = validated_data.get('secondary_image', instance.secondary_image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.pledge_type_id = validated_data.get('pledge_type_id', instance.pledge_type_id)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance