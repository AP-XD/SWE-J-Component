# Generated by Django 4.0 on 2022-04-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_admin_phone_no_staffs_phone_no_students_phone_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffs',
            name='subject',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
