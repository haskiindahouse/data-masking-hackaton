# Generated by Django 4.2.8 on 2023-12-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0012_alter_queryfavorite_query_alter_queryfavorite_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='querylog',
            name='error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='querylog',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]
