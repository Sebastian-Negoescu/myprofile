# Generated by Django 3.0.2 on 2020-01-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myjobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
    ]