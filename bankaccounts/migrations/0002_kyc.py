# Generated by Django 4.2.4 on 2023-09-04 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankaccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kyc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='kyc/')),
                ('marital_status', models.CharField(choices=[['single', 'SINGLE'], ['married', 'MARRIED'], ['others', 'OTHERS']], max_length=100)),
                ('gender', models.CharField(choices=[['male', 'MALE'], ['female', 'FEMALE'], ['others', 'OTHERS']], max_length=100)),
                ('identity_type', models.CharField(choices=[['pan_card', 'PANCARD'], ['aadhar', 'AADHAR'], ['passport', 'PASSPORT'], ['driving_liscence', 'DRIVING_LISCENCE'], ['others', 'OTHERS']], max_length=100)),
                ('identity_image', models.ImageField(upload_to='kyc/')),
                ('date_of_birth', models.DateTimeField()),
                ('signature', models.ImageField(upload_to='kyc/')),
                ('country', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bankaccounts.account')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
