# Generated by Django 4.0 on 2022-01-04 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('client', '0003_alter_client_sales_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
    ]
