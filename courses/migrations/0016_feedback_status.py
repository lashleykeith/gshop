# Generated by Django 3.2.5 on 2021-07-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_teachercomments_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('great_job', 'Great Job'), ('well_done', 'Well Done'), ('good_try', 'Good Try'), ('need_practivce', 'Need More Practice')], max_length=50, null=True),
        ),
    ]
