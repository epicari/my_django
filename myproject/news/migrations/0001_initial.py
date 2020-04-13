# Generated by Django 3.0.5 on 2020-04-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_heading', models.CharField(max_length=250)),
                ('news_body', models.TextField()),
            ],
        ),
    ]
