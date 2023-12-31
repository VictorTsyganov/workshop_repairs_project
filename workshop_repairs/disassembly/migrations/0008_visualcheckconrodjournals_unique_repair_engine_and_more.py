# Generated by Django 4.1.7 on 2023-06-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disassembly', '0007_remove_minmaxvalue_unique_min_max'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='visualcheckconrodjournals',
            constraint=models.UniqueConstraint(fields=('engine_number', 'repair'), name='unique_repair_engine'),
        ),
        migrations.AddConstraint(
            model_name='visualcheckmainjournals',
            constraint=models.UniqueConstraint(fields=('engine_number', 'repair'), name='unique_rep_eng'),
        ),
    ]
