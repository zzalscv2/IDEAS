# Generated by Django 3.0.4 on 2021-02-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_project_fork_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='branch',
            field=models.CharField(default='master', max_length=128),
        ),
        migrations.AlterField(
            model_name='commit',
            name='hash',
            field=models.CharField(max_length=128),
        ),
    ]
