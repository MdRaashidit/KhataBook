# Generated by Django 3.1.2 on 2021-02-07 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udhaar', '0004_transactions_credit_debit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='party',
            name='dbnumber',
        ),
    ]
