# Generated by Django 4.0.5 on 2022-07-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
