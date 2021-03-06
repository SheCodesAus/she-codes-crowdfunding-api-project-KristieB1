# Generated by Django 4.0.2 on 2022-03-22 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_category_category_name_pledgetype_pledge_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='project',
        ),
        migrations.RemoveField(
            model_name='pledgetype',
            name='pledge',
        ),
        migrations.AddField(
            model_name='pledge',
            name='pledge_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pledge_id', to='projects.pledgetype'),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='projects.category'),
        ),
    ]
