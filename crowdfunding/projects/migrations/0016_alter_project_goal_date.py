# Generated by Django 4.0.2 on 2022-05-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_alter_project_goal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goal_date',
            field=models.DateField(),
        ),
    ]