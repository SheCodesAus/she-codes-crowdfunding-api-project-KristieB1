# Generated by Django 4.0.2 on 2022-05-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_remove_pledge_pledge_type_remove_project_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='goal_date',
            field=models.DateField(),
        ),
    ]
