from django.contrib.auth import get_user_model
from django.db import models

from journal_repairs.models import Repair, EngineNumber

User = get_user_model()


class AcceptanceAggregate(models.Model):
    pub_date = models.DateTimeField(
        verbose_name = 'Дата приемки.',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.PROTECT,
        related_name='aggregates',
        verbose_name = 'Сотрудник производивший приемку.'
    )
    repair = models.ForeignKey(
        Repair,
        on_delete=models.PROTECT,
        related_name='aggregates',
        verbose_name = 'Номер заявки на ремонт.'
    )
    engine_number = models.ForeignKey(
        EngineNumber,
        on_delete=models.PROTECT,
        related_name='aggregates',
        verbose_name = 'Номер ДВС на приемке.'
    )
    transport_frame = models.BooleanField(
        null=True, default=False,
        verbose_name = 'Рама двигателя.'
    )
    transport_frame_com = models.CharField(
        max_length=50, blank=True, null=True,
        verbose_name = 'Комментарий о раме.',
        help_text = 'Добавляйте описание при необходимости.'
    )
    damper = models.BooleanField(
        null=True, default=False,
        verbose_name = 'Демпфер ДВС.'
    )
    damper_count = models.PositiveIntegerField(
        blank=True, null=True,
        verbose_name = 'Количество демпферов.',
        help_text = 'Укажите если не все в наличии.'
    )
    cylinder_head = models.BooleanField(
        null=True, default=False,
        verbose_name = 'Головки цилиндра.'
    )
    cylinder_head_count = models.PositiveIntegerField(
        blank=True, null=True,
        verbose_name = 'Количество ГБЦ.',
        help_text = 'Укажите если не все в наличии.'
    )
    fuel_pump = models.BooleanField(
        null=True, default=False,
        verbose_name = 'Топливный насос.'
    )
    fuel_pump_count = models.PositiveIntegerField(
        blank=True, null=True,
        verbose_name = 'Количество ТН.',
        help_text = 'Укажите если не все в наличии.'
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name = 'Примечания.',
        help_text = 'Добавляйте при необходимости.'
    )

    def __str__(self):
        return f'Приемка ЗР {self.repair} ДВС № {self.engine_number}.'
    
    class Meta:
        ordering = ('-pub_date',)


class Image(models.Model):
    image = models.ImageField(
        verbose_name = 'Фото на приемке',
        upload_to='posts/',
        blank=True,
        null=True,
    )
    pub_date = models.DateTimeField(
        verbose_name = 'Дата фото.',
        auto_now_add=True
    )
    acceptance_aggregate = models.ForeignKey(
        AcceptanceAggregate,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name = 'Приемка на ремонт.'
    )

    def __str__(self):
        return f'Фото на приемке {self.acceptance_aggregate} {self.image}.'
    
    class Meta:
        ordering = ('-pub_date',)
