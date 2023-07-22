# Generated by Django 4.2.3 on 2023-07-22 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_amount', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.bankaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LimitPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.currency')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datetime', models.DateTimeField()),
                ('budget_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.budget')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.transactioncategory')),
                ('description_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.description')),
                ('payment_method_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.paymentmethod')),
                ('transaction_type_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.transactiontype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='cash_amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.wallet'),
        ),
        migrations.AddField(
            model_name='budget',
            name='limit_period_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='finance.limitperiod'),
        ),
        migrations.AddField(
            model_name='budget',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='currency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.currency'),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
