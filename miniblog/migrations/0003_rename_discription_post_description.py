# Generated by Django 5.0 on 2024-02-05 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0002_alter_post_discription_alter_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='discription',
            new_name='description',
        ),
    ]
