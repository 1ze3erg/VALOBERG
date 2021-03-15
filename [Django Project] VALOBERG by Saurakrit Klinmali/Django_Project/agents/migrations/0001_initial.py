# Generated by Django 3.1.7 on 2021-03-01 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='../uploads/agents')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='../uploads/agents')),
                ('name', models.CharField(max_length=200, null=True)),
                ('origin', models.CharField(max_length=200, null=True)),
                ('bio', models.TextField(null=True)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agents.role')),
            ],
        ),
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='../uploads/abilities')),
                ('name', models.CharField(max_length=200, null=True)),
                ('creds', models.CharField(max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=200)),
                ('ult_points', models.PositiveSmallIntegerField(blank=True)),
                ('detail', models.TextField(null=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agents.agent')),
            ],
        ),
    ]
