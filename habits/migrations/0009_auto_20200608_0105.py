# Generated by Django 3.0.6 on 2020-06-08 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0008_auto_20200608_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='recorded_on',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
