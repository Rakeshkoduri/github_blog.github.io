# Generated by Django 4.1.4 on 2023-01-12 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogmodel_upload_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='image',
        ),
    ]
