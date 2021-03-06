# Generated by Django 3.2 on 2022-02-20 21:59

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_code',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='perm',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
