# Generated by Django 4.1.7 on 2023-03-24 14:37

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('journal_repairs', '0003_alter_customer_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercontact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]