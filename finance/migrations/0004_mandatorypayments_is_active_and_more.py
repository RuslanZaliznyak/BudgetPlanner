# Generated by Django 4.2.3 on 2023-07-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_mandatorypayments'),
    ]

    operations = [
        migrations.AddField(
            model_name='mandatorypayments',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mandatorypayments',
            name='payment_day',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='mandatorypayments',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mandatorypayments',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
