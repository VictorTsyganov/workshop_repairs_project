from django.contrib.auth import get_user_model
from django.db import models

from journal_repairs.models import Repair, EngineNumber

User = get_user_model()


CHOICES = (
    ('Без изъянов', 'Без изъянов'),
    ('Царапина допустимая', 'Царапина допустимая'),
    ('Царапина не допустимая', 'Царапина не допустимая'),
    ('Кавитация', 'Кавитация'),
    ('Коррозия', 'Коррозия'),
    ('Волнистая поверхность', 'Волнистая поверхность'),
    ('Трещина', 'Трещина'),
)


class VisualCheckConRodJournals(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата проверки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='vc_con_rod_journals',
        verbose_name='Сотрудник производивший проверку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='vc_con_rod_journals',
        verbose_name='Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='vc_con_rod_journals',
        verbose_name='Номер ДВС.'
    )
    con_journal_1 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='1-ая шатунная'
    )
    con_journal_2 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='2-ая шатунная'
    )
    con_journal_3 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='3-я шатунная'
    )
    con_journal_4 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='4-ая шатунная'
    )
    con_journal_5 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='5-ая шатунная'
    )
    con_journal_6 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='6-ая шатунная'
    )
    con_journal_7 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='7-ая шатунная'
    )
    con_journal_8 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='8-ая шатунная'
    )
    con_journal_9 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='9-ая шатунная'
    )
    con_journal_10 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='10-ая шатунная'
    )

    def __str__(self):
        return (f'Проверка коленчатого вала '
                f'ЗР {self.repair} ДВС № {self.engine_number}.')

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['engine_number', 'repair'], name='unique_repair_engine')
        ]


class VisualCheckMainJournals(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата проверки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='vc_main_journals',
        verbose_name='Сотрудник производивший проверку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='vc_main_journals',
        verbose_name='Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='vc_main_journals',
        verbose_name='Номер ДВС.'
    )
    main_journal_1 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='1-ая коренная'
    )
    main_journal_2 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='2-ая коренная'
    )
    main_journal_3 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='3-я коренная'
    )
    main_journal_4 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='4-ая коренная'
    )
    main_journal_5 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='5-ая коренная'
    )
    main_journal_6 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='6-ая коренная'
    )
    main_journal_7 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='7-ая коренная'
    )
    main_journal_8 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='8-ая коренная'
    )
    main_journal_9 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='9-ая коренная'
    )
    main_journal_10 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='10-ая коренная'
    )
    main_journal_11 = models.CharField(
        max_length=50,
        null=True, blank=True,
        choices=CHOICES,
        verbose_name='11-ая коренная'
    )

    def __str__(self):
        return (f'Визуальная проверка коренных шеек КВ '
                f'ЗР {self.repair} ДВС № {self.engine_number}.')

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['engine_number', 'repair'], name='unique_rep_eng')
        ]


class CheckСounterweightTorque(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата проверки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='counterweight_torque',
        verbose_name='Сотрудник производивший проверку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='counterweight_torque',
        verbose_name='Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='counterweight_torque',
        verbose_name='Номер ДВС.'
    )
    vc_con_rod_journsls = models.ForeignKey(
        VisualCheckConRodJournals,
        on_delete=models.CASCADE,
        related_name='counterweight_torque',
        verbose_name='Визуальная проверка шатунных шеек.'
    )
    torque = models.CharField(
        max_length=20,
        null=True, blank=True,
        verbose_name='Заданный момент затяжки.'
    )
    counterweight_1 = models.BooleanField(
        null=True, blank=True,
        verbose_name='1-ый противовес'
    )
    counterweight_2 = models.BooleanField(
        null=True, blank=True,
        verbose_name='2-ой противовес'
    )
    counterweight_3 = models.BooleanField(
        null=True, blank=True,
        verbose_name='3-ий противовес'
    )
    counterweight_4 = models.BooleanField(
        null=True, blank=True,
        verbose_name='4-ый противовес'
    )
    counterweight_5 = models.BooleanField(
        null=True, blank=True,
        verbose_name='5-ый противовес'
    )
    counterweight_6 = models.BooleanField(
        null=True, blank=True,
        verbose_name='6-ой противовес'
    )
    counterweight_7 = models.BooleanField(
        null=True, blank=True,
        verbose_name='7-ой противовес'
    )
    counterweight_8 = models.BooleanField(
        null=True, blank=True,
        verbose_name='8-ой противовес'
    )
    counterweight_9 = models.BooleanField(
        null=True, blank=True,
        verbose_name='9-ый противовес'
    )
    counterweight_10 = models.BooleanField(
        null=True, blank=True,
        verbose_name='10-ый противовес'
    )
    counterweight_11 = models.BooleanField(
        null=True, blank=True,
        verbose_name='11-ый противовес'
    )

    def __str__(self):
        return (f'Проверка моментов затяжки противовесов КВ '
                f'ЗР {self.repair} ДВС № {self.engine_number}.')

    class Meta:
        ordering = ('-pub_date',)


class MinMaxValue(models.Model):
    min_val = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='Минимальное значение'
    )
    max_val = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='Максимальное значение'
    )
    unit = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='Единица измерения'
    )
    measuring_tool = models.CharField(
        max_length=100,
        null=True, blank=True,
        verbose_name='Измерительный инструмент'
    )


class MeasuringConRodJournals(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата проверки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='ms_con_rod_journals',
        verbose_name='Сотрудник производивший проверку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='ms_con_rod_journals',
        verbose_name='Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='ms_con_rod_journals',
        verbose_name='Номер ДВС.'
    )
    min_max_value = models.ForeignKey(
        MinMaxValue,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='ms_con_rod_journals',
        verbose_name='Минимальное и максимальное занчения'
    )
    con_journal_1_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='1-ая шатунная (замер)'
    )
    con_journal_2_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='2-ая шатунная (замер)'
    )
    con_journal_3_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='3-я шатунная (замер)'
    )
    con_journal_4_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='4-ая шатунная (замер)'
    )
    con_journal_5_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='5-ая шатунная (замер)'
    )
    con_journal_6_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='6-ая шатунная (замер)'
    )
    con_journal_7_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='7-ая шатунная (замер)'
    )
    con_journal_8_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='8-ая шатунная (замер)'
    )
    con_journal_9_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='9-ая шатунная (замер)'
    )
    con_journal_10_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='10-ая шатунная (замер)'
    )

    def __str__(self):
        return (f'Измерение шатунных шеек КВ '
                f'ЗР {self.repair} ДВС № {self.engine_number}.')

    class Meta:
        ordering = ('-pub_date',)


class MeasuringMainJournals(models.Model):
    pub_date = models.DateTimeField(
        verbose_name='Дата проверки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='ms_main_journals',
        verbose_name='Сотрудник производивший проверку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='ms_main_journals',
        verbose_name='Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='ms_main_journals',
        verbose_name='Номер ДВС.'
    )
    min_max_value = models.ForeignKey(
        MinMaxValue,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='ms_main_journals',
        verbose_name='Минимальное и максимальное занчения'
    )
    main_journal_1_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='1-ая коренная (замер)'
    )
    main_journal_2_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='2-ая коренная (замер)'
    )
    main_journal_3_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='3-я коренная (замер)'
    )
    main_journal_4_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='4-ая коренная (замер)'
    )
    main_journal_5_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='5-ая коренная (замер)'
    )
    main_journal_6_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='6-ая коренная (замер)'
    )
    main_journal_7_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='7-ая коренная (замер)'
    )
    main_journal_8_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='8-ая коренная (замер)'
    )
    main_journal_9_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='9-ая коренная (замер)'
    )
    main_journal_10_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='10-ая коренная (замер)'
    )
    main_journal_11_meas = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name='11-ая коренная (замер)'
    )

    def __str__(self):
        return (f'Измерение коренных шеек КВ '
                f'ЗР {self.repair} ДВС № {self.engine_number}.')

    class Meta:
        ordering = ('-pub_date',)


class ImageCrankshaft(models.Model):
    image = models.ImageField(
        verbose_name = 'Фото дефектов коленчатого вала',
        upload_to='crankshaft/',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        verbose_name = 'Дата фото.',
        auto_now_add=True
    )
    vc_con_rod_journsls = models.ForeignKey(
        VisualCheckConRodJournals,
        on_delete=models.CASCADE,
        related_name='crankshaft_images',
        verbose_name = 'Фото дефектов коленчатого вала'
    )

    def __str__(self):
        return f'Фото дефектов коленчатого вала {self.vc_con_rod_journsls}.'
    
    class Meta:
        ordering = ('-pub_date',)
