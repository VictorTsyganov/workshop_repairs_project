# Generated by Django 4.2.3 on 2023-07-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disassembly', '0008_visualcheckconrodjournals_unique_repair_engine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkсounterweighttorque',
            name='vc_con_rod_journsls',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='counterweight_torque', to='disassembly.visualcheckconrodjournals', verbose_name='Визуальная проверка шатунных шеек.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measuringconrodjournals',
            name='min_max_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ms_con_rod_journals', to='disassembly.minmaxvalue', verbose_name='Минимальное и максимальное занчения'),
        ),
        migrations.AlterField(
            model_name='measuringmainjournals',
            name='min_max_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ms_main_journals', to='disassembly.minmaxvalue', verbose_name='Минимальное и максимальное занчения'),
        ),
    ]
