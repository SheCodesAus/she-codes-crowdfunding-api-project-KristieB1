# Generated by Django 4.0.2 on 2022-05-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_alter_project_secondary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
