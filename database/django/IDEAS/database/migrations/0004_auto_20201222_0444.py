# Generated by Django 3.0.4 on 2020-12-22 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20201221_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['id'], 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterModelOptions(
            name='commit',
            options={'ordering': ['id'], 'verbose_name': 'commit', 'verbose_name_plural': 'commits'},
        ),
        migrations.AlterModelOptions(
            name='diff',
            options={'ordering': ['id'], 'verbose_name': 'diff', 'verbose_name_plural': 'diffs'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id'], 'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AlterModelOptions(
            name='projectauthor',
            options={'ordering': ['id'], 'verbose_name': 'project has author', 'verbose_name_plural': 'project has authors'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='diff',
            order_with_respect_to=None,
        ),
    ]
