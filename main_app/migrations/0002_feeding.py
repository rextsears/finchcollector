# Generated by Django 4.2.5 on 2023-09-14 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('food_type', models.CharField(max_length=100)),
                ('finch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedings', to='main_app.finch')),
            ],
        ),
    ]
