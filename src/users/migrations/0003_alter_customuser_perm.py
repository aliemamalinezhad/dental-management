# Generated by Django 3.2 on 2022-02-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220220_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='perm',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
