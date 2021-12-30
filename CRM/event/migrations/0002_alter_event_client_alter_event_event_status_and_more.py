# Generated by Django 4.0 on 2021-12-30 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('contract', '0003_alter_contract_client'),
        ('client', '0002_alter_client_sales_contact'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract'),
        ),
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
        ),
    ]