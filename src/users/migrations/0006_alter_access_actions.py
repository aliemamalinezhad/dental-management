# Generated by Django 3.2 on 2022-02-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='actions',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
