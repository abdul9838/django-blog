# Generated by Django 5.0 on 2024-02-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='discription',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
