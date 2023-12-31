# Generated by Django 4.1.7 on 2023-04-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_repairs', '0012_alter_enginenumber_equipment_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repair',
            name='engine_hours',
        ),
        migrations.AlterField(
            model_name='enginehours',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AddConstraint(
            model_name='enginehours',
            constraint=models.UniqueConstraint(fields=('pub_date', 'engine_hours'), name='unique_date_hours'),
        ),
    ]
