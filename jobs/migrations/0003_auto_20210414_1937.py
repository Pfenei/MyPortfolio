# Generated by Django 2.1 on 2021-04-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210414_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='imageurl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='iconurl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
