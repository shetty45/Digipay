# Generated by Django 4.2.4 on 2023-09-20 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0003_alter_transaction_updated_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='receiver_amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender_amount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_account', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
