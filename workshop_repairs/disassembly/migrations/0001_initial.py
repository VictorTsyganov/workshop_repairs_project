# Generated by Django 4.1.7 on 2023-05-18 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal_repairs', '0016_rename_customer_enginenumber_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisualCheckMainJournals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проверки.')),
                ('main_journal_1', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='1-ая коренная')),
                ('main_journal_2', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='2-ая коренная')),
                ('main_journal_3', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='3-я коренная')),
                ('main_journal_4', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='4-ая коренная')),
                ('main_journal_5', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='5-ая коренная')),
                ('main_journal_6', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='6-ая коренная')),
                ('main_journal_7', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='7-ая коренная')),
                ('main_journal_8', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='8-ая коренная')),
                ('main_journal_9', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='9-ая коренная')),
                ('main_journal_10', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='10-ая коренная')),
                ('main_journal_11', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='11-ая коренная')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vc_main_journals', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник производивший проверку.')),
                ('engine_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vc_main_journals', to='journal_repairs.enginenumber', verbose_name='Номер ДВС.')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vc_main_journals', to='journal_repairs.repair', verbose_name='Номер заявки на ремонт.')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='VisualCheckConRodJournals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проверки.')),
                ('con_journal_1', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='1-ая шатунная')),
                ('con_journal_2', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='2-ая шатунная')),
                ('con_journal_3', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='3-я шатунная')),
                ('con_journal_4', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='4-ая шатунная')),
                ('con_journal_5', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='5-ая шатунная')),
                ('con_journal_6', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='6-ая шатунная')),
                ('con_journal_7', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='7-ая шатунная')),
                ('con_journal_8', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='8-ая шатунная')),
                ('con_journal_9', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='9-ая шатунная')),
                ('con_journal_10', models.CharField(blank=True, choices=[('Без изъянов', 'Без изъянов'), ('Царапина допустимая', 'Царапина допустимая'), ('Царапина не допустимая', 'Царапина не допустимая'), ('Кавитация', 'Кавитация'), ('Коррозия', 'Коррозия'), ('Волнистая поверхность', 'Волнистая поверхность'), ('Трещина', 'Трещина')], max_length=50, null=True, verbose_name='10-ая шатунная')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vc_con_rod_journals', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник производивший проверку.')),
                ('engine_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vc_con_rod_journals', to='journal_repairs.enginenumber', verbose_name='Номер ДВС.')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vc_con_rod_journals', to='journal_repairs.repair', verbose_name='Номер заявки на ремонт.')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='MeasuringMainJournals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проверки.')),
                ('main_journal_1', models.FloatField(blank=True, null=True, verbose_name='1-ая коренная')),
                ('main_journal_2', models.FloatField(blank=True, null=True, verbose_name='2-ая коренная')),
                ('main_journal_3', models.FloatField(blank=True, null=True, verbose_name='3-я коренная')),
                ('main_journal_4', models.FloatField(blank=True, null=True, verbose_name='4-ая коренная')),
                ('main_journal_5', models.FloatField(blank=True, null=True, verbose_name='5-ая коренная')),
                ('main_journal_6', models.FloatField(blank=True, null=True, verbose_name='6-ая коренная')),
                ('main_journal_7', models.FloatField(blank=True, null=True, verbose_name='7-ая коренная')),
                ('main_journal_8', models.FloatField(blank=True, null=True, verbose_name='8-ая коренная')),
                ('main_journal_9', models.FloatField(blank=True, null=True, verbose_name='9-ая коренная')),
                ('main_journal_10', models.FloatField(blank=True, null=True, verbose_name='10-ая коренная')),
                ('main_journal_11', models.FloatField(blank=True, null=True, verbose_name='11-ая коренная')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ms_main_journals', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник производивший проверку.')),
                ('engine_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ms_main_journals', to='journal_repairs.enginenumber', verbose_name='Номер ДВС.')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ms_main_journals', to='journal_repairs.repair', verbose_name='Номер заявки на ремонт.')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='MeasuringConRodJournals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проверки.')),
                ('con_journal_1', models.FloatField(blank=True, null=True, verbose_name='1-ая шатунная')),
                ('con_journal_2', models.FloatField(blank=True, null=True, verbose_name='2-ая шатунная')),
                ('con_journal_3', models.FloatField(blank=True, null=True, verbose_name='3-я шатунная')),
                ('con_journal_4', models.FloatField(blank=True, null=True, verbose_name='4-ая шатунная')),
                ('con_journal_5', models.FloatField(blank=True, null=True, verbose_name='5-ая шатунная')),
                ('con_journal_6', models.FloatField(blank=True, null=True, verbose_name='6-ая шатунная')),
                ('con_journal_7', models.FloatField(blank=True, null=True, verbose_name='7-ая шатунная')),
                ('con_journal_8', models.FloatField(blank=True, null=True, verbose_name='8-ая шатунная')),
                ('con_journal_9', models.FloatField(blank=True, null=True, verbose_name='9-ая шатунная')),
                ('con_journal_10', models.FloatField(blank=True, null=True, verbose_name='10-ая шатунная')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ms_con_rod_journals', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник производивший проверку.')),
                ('engine_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ms_con_rod_journals', to='journal_repairs.enginenumber', verbose_name='Номер ДВС.')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ms_con_rod_journals', to='journal_repairs.repair', verbose_name='Номер заявки на ремонт.')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='CheckСounterweightTorque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата проверки.')),
                ('torque', models.FloatField(blank=True, null=True, verbose_name='Заданный момент затяжки.')),
                ('counterweight_1', models.BooleanField(blank=True, null=True, verbose_name='1-ый противовес')),
                ('counterweight_2', models.BooleanField(blank=True, null=True, verbose_name='2-ой противовес')),
                ('counterweight_3', models.BooleanField(blank=True, null=True, verbose_name='3-ий противовес')),
                ('counterweight_4', models.BooleanField(blank=True, null=True, verbose_name='4-ый противовес')),
                ('counterweight_5', models.BooleanField(blank=True, null=True, verbose_name='5-ый противовес')),
                ('counterweight_6', models.BooleanField(blank=True, null=True, verbose_name='6-ой противовес')),
                ('counterweight_7', models.BooleanField(blank=True, null=True, verbose_name='7-ой противовес')),
                ('counterweight_8', models.BooleanField(blank=True, null=True, verbose_name='8-ой противовес')),
                ('counterweight_9', models.BooleanField(blank=True, null=True, verbose_name='9-ый противовес')),
                ('counterweight_10', models.BooleanField(blank=True, null=True, verbose_name='10-ый противовес')),
                ('counterweight_11', models.BooleanField(blank=True, null=True, verbose_name='11-ый противовес')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='counterweight_torque', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник производивший проверку.')),
                ('engine_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='counterweight_torque', to='journal_repairs.enginenumber', verbose_name='Номер ДВС.')),
                ('repair', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='counterweight_torque', to='journal_repairs.repair', verbose_name='Номер заявки на ремонт.')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
