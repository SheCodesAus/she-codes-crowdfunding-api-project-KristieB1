# Generated by Django 4.0.2 on 2022-05-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_project_date_created_alter_project_goal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
