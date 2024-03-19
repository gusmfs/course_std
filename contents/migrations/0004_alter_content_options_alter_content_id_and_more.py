# Generated by Django 5.0.1 on 2024-01-10 21:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_alter_content_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={},
        ),
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='video_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
