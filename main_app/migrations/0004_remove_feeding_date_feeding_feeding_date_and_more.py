# Generated by Django 4.2.5 on 2023-09-15 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_finch_toys'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeding',
            name='date',
        ),
        migrations.AddField(
            model_name='feeding',
            name='feeding_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Feeding Date'),
        ),
        migrations.AddField(
            model_name='feeding',
            name='notes',
            field=models.CharField(default=None, max_length=255, verbose_name='Notes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feeding',
            name='food_type',
            field=models.CharField(max_length=100, verbose_name='Food Type'),
        ),
    ]
