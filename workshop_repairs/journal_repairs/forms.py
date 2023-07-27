from django import forms
from django_select2 import forms as s2forms

from .models import (Comment, EngineHours, EngineNumber, EngineNumberRepair,
                     Repair)


class CustomerWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'name__icontains',
    ]


class CustomerContactWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'name__icontains',
        'last_name__icontains',
    ]


class RepairTypeWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'title__icontains',
    ]


class EngineNumberWidger(s2forms.ModelSelect2Widget):
    search_fields = [
        'engine_number__icontains',
    ]


class ExtraEngineNumberWidger(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        'engine_number__icontains',
    ]


class AddressOperationWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        'address__icontains',
    ]


class EquipmentWidger(s2forms.ModelSelect2Widget):
    search_fields = [
        'name_equipment__icontains',
    ]


class RepairNumberWidger(s2forms.ModelSelect2Widget):
    search_fields = [
        'repair_number__icontains',
    ]


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair

        labels = {'repair_number': 'Номер заявки на ремонт.',
                  'customer': 'Заказчик ремонта.',
                  'repair_type': 'Тип ремонта.',
                  'customer_contacts': 'Контактное лицо.',
                  'address': 'Место эксплуатации.',
                  'description': 'Описание ремонта.'
                  }
        help_texts = {'repair_number': 'Только цифры.',
                      'customer': 'Чувствительно к регистру.',
                      'repair_type': 'Чувствительно к регистру.',
                      'customer_contacts': 'Чувствительно к регистру.',
                      'address': ('Чувствительно к регистру. '
                                  'Короткое название объекта.'),
                      'description': 'Описание неисправности и примечания.'
                      }
        fields = ['repair_number',
                  'repair_type', 'customer',
                  'customer_contacts', 'address',
                  'description']
        widgets = {
            'customer': CustomerWidget,
            'repair_type': RepairTypeWidget,
            'customer_contacts': CustomerContactWidget,
            'address': AddressOperationWidget,
        }


class EngineNumberForm(forms.ModelForm):
    class Meta:
        model = EngineNumber

        labels = {'engine_number': 'Номер нового ДВС.',
                  'engine': 'Модель двигателя.',
                  'equipment': 'Оборудование, на котором установлен ДВС.',
                  'owner': 'Владелец ДВС.',
                  'address': 'Место нахождения владельца оборудования.',
                  'equipment_number': 'Серийный номер оборудования.',
                  'start_date': 'Дата ввода в эксплуатацию.',
                  }
        help_texts = {'engine': 'Чувствительно к регистру.',
                      'equipment': 'Чувствительно к регистру.',
                      'owner': 'Чувствительно к регистру.',
                      'address': ('Чувствительно к регистру. '
                                  'Короткое название объекта.'),
                      }
        fields = ['engine_number', 'engine',
                  'equipment', 'owner',
                  'address', 'equipment_number',
                  'start_date']
        widgets = {
            'engine': RepairTypeWidget,
            'equipment': RepairTypeWidget,
            'owner': CustomerWidget,
            'address': AddressOperationWidget,
        }


class EngineHoursForm(forms.ModelForm):
    class Meta:
        model = EngineHours

        labels = {'engine_number': 'Номер ремонтируемого ДВС.',
                  'engine_hours': 'Наработка ДВС (м.ч. или км.).',
                  }
        help_texts = {'engine_hours': 'Только цифры.', }
        fields = ['engine_number', 'engine_hours',]
        widgets = {
            'engine_number': EngineNumberWidger,
        }


class EngineNumberRepairForm(forms.ModelForm):
    class Meta:
        model = EngineNumberRepair

        labels = {'engine_number': 'Номер ДВС.',
                  'repair': 'Номер заявки на ремонт.',
                  }
        fields = ['repair', 'engine_number',]
        widgets = {
            'repair': RepairNumberWidger,
            'engine_number': EngineNumberWidger,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {'text': 'Примечание к данному ремонту.'}
        help_texts = {'text': 'Здесь можно указать любые примечания.'}
        fields = ['text']
