# Generated by Django 4.0 on 2022-01-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateTimeField(),
        ),
    ]
