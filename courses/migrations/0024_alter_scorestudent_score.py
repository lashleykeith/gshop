# Generated by Django 3.2.5 on 2021-08-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_auto_20210801_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorestudent',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
