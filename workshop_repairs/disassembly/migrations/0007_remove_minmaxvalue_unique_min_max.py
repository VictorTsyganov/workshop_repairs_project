# Generated by Django 4.1.7 on 2023-06-22 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disassembly', '0006_remove_measuringmainjournals_main_journal_1_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='minmaxvalue',
            name='unique_min_max',
        ),
    ]
