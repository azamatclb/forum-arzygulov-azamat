# Generated by Django 5.0.7 on 2024-08-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_topic_title_alter_topic_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Тема'),
        ),
    ]
