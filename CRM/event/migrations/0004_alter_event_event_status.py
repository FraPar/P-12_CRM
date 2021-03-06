# Generated by Django 4.0 on 2022-01-10 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0005_alter_contract_status'),
        ('event', '0003_alter_event_date_updated_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contract', to_field='status'),
        ),
    ]
