# from turtle import title
# from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import CharField

# Create your models here.

class PledgeType(models.Model):
    pledge_type_name =models.CharField(max_length=200)
    
    

class Category(models.Model):
    category_name = models.CharField(max_length=200)
   

class Project(models.Model):
    title = models.CharField(max_length=200)
    blurb = models.TextField()
    description = models.TextField()
    goal = models.IntegerField()
    goal_date = models.DateTimeField()
    progress = models.IntegerField()
    primary_image= models.URLField()
    secondary_image = models.URLField()
    status = models.CharField(max_length=200)
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='project_id'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

    pledge_type = models.ForeignKey(
        'PledgeType',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='pledge_id'
    )

   
