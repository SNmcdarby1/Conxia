# Generated by Django 2.2.6 on 2020-03-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
