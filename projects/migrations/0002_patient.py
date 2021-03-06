# Generated by Django 3.2.6 on 2021-09-09 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, max_length=200, null=True)),
                ('patient_age', models.IntegerField(blank=True, null=True)),
                ('Marital_status', models.CharField(blank=True, max_length=200, null=True)),
                ('Primanry_Issue', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('Secondary_Issue', models.CharField(blank=True, max_length=200, null=True)),
                ('description_secondary', models.TextField(blank=True, null=True)),
                ('Dependant', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['patient_name'],
            },
        ),
    ]
