# Generated by Django 3.1.4 on 2021-01-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='subject',
            field=models.CharField(default='Science', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
