# Generated by Django 3.0.4 on 2020-04-05 09:52

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
            name='PrivatPaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=1)),
                ('message', models.CharField(max_length=200)),
                ('amt', models.CharField(max_length=100)),
                ('ccy', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='YandexPaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('codepro', models.CharField(max_length=10)),
                ('label', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField(auto_now=True)),
                ('datetime_end', models.DateTimeField()),
                ('content', models.TextField(max_length=512)),
                ('wn8', models.IntegerField(default=0)),
                ('wins_percent', models.IntegerField(default=0)),
                ('tag', models.CharField(max_length=7, null=True)),
                ('url_clan', models.CharField(max_length=150)),
                ('status', models.BooleanField(choices=[(True, 'Payed'), (False, 'Not payed')], default=False, max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
