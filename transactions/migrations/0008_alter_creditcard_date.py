# Generated by Django 4.2.4 on 2023-10-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='date',
            field=models.DateField(),
        ),
    ]
