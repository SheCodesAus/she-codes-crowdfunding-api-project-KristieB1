# Generated by Django 4.0.2 on 2022-03-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_pledge_pledge_type_remove_project_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='Misc', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledgetype',
            name='pledge_type_name',
            field=models.CharField(default='financial', max_length=200),
            preserve_default=False,
        ),
    ]
