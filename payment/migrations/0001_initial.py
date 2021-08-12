# Generated by Django 3.2.5 on 2021-08-02 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_client_employee_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=15)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('service', models.CharField(blank=True, max_length=50, null=True)),
                ('stylist', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('bill', models.CharField(blank=True, default=0.0, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MONTHLY', 'MONTHLY'), ('HOURLY', 'HOURLY')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.employee')),
            ],
        ),
    ]
