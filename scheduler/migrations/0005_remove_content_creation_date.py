# Generated by Django 3.2.10 on 2022-01-15 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_post_strategy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='creation_date',
        ),
    ]
