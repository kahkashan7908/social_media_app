# Generated by Django 3.0.5 on 2023-08-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postmodel_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
