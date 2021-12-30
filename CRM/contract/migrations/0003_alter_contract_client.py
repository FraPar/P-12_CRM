# Generated by Django 4.0 on 2021-12-30 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_sales_contact'),
        ('contract', '0002_alter_contract_sales_contact_alter_contract_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
