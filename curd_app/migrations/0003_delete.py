# Generated by Django 2.2.5 on 2020-06-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd_app', '0002_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='delete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]