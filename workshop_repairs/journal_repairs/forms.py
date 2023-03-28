from django import forms

from .models import Repair


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        
        labels = {'repair_number': 'Номер заявки на ремонт',
                  'customer': 'Заказчик', 'repair_type': 'Тип ремонта',
                  'engine': 'Модель ДВС', 'engine_number': 'Номер ДВС',
                  'customer_contacts': 'Контактное лицо',
                  'description': 'Примечания'
                  }
        fields = ['repair_number', 'customer',
                  'repair_type', 'engine', 'engine_number',
                  'customer_contacts', 'description']
