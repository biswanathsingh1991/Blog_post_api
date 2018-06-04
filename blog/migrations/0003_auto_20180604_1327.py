# Generated by Django 2.0.5 on 2018-06-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180529_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
