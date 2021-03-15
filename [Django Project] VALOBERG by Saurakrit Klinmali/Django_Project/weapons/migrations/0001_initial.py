# Generated by Django 3.1.7 on 2021-03-01 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='../uploads/weapons')),
                ('name', models.CharField(max_length=200, null=True)),
                ('fire_mode', models.CharField(max_length=200, null=True)),
                ('creds', models.CharField(max_length=200, null=True)),
                ('magazine', models.PositiveSmallIntegerField(null=True)),
                ('types', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weapons.type')),
            ],
        ),
        migrations.CreateModel(
            name='Skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='../uploads/skins')),
                ('collection', models.CharField(max_length=200, null=True)),
                ('unlock', models.CharField(max_length=200, null=True)),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon')),
            ],
        ),
    ]