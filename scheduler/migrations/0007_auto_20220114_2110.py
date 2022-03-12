# Generated by Django 3.2.10 on 2022-01-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_auto_20220114_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(blank=True, max_length=9999),
        ),
        migrations.AddField(
            model_name='post',
            name='nsfw',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='scheduled_for',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='strategy',
            field=models.CharField(choices=[('NOW', 'Now'), ('CUSTOM', 'Custom')], default='CUSTOM', max_length=6),
        ),
        migrations.AlterField(
            model_name='content',
            name='kind',
            field=models.CharField(choices=[('LINK', 'Link'), ('TEXT', 'Text'), ('MEDIA', 'Media')], default='LINK', max_length=5),
        ),
        migrations.DeleteModel(
            name='Strategy',
        ),
    ]