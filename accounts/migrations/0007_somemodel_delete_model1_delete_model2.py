# Generated by Django 4.0.5 on 2022-07-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_model1_model2'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Model1',
        ),
        migrations.DeleteModel(
            name='Model2',
        ),
    ]