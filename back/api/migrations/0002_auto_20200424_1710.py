# Generated by Django 3.0.5 on 2020-04-24 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='default', max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='short_name',
            field=models.CharField(default='default', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.TextField(default='default name', max_length=300),
        ),
        migrations.AlterField(
            model_name='file',
            name='course',
            field=models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.Course', to_field='short_name'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(default='default', max_length=300),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=500)),
                ('description', models.TextField(default='no description')),
                ('link', models.TextField(default='https://www.google.com')),
                ('course', models.ForeignKey(db_column='course', on_delete=django.db.models.deletion.CASCADE, related_name='links', to='api.Course', to_field='short_name')),
            ],
        ),
    ]
