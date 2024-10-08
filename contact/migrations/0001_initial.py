# Generated by Django 5.1 on 2024-09-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessagesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Message List',
                'verbose_name_plural': 'Messages List',
                'ordering': ('-id',),
            },
        ),
    ]
