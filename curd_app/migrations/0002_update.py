# Generated by Django 2.2.5 on 2020-06-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]