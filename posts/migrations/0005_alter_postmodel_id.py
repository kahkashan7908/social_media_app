# Generated by Django 4.1 on 2023-08-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230823_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
