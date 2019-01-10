# Generated by Django 2.1.3 on 2019-01-09 22:51

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('caption', models.TextField()),
                ('design_type', models.CharField(choices=[('2d', '2D'), ('2d', '3D')], max_length=5)),
                ('pic', models.ImageField(upload_to=gallery.models.picture_directory_path)),
                ('description', models.TextField()),
                ('time_completed', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender_ip', models.GenericIPAddressField()),
            ],
        ),
    ]
