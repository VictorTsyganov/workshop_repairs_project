from django import forms
from django_select2 import forms as s2forms
from multiupload.fields import MultiImageField

from .models import (VisualCheckConRodJournals, VisualCheckMainJournals,
                     CheckСounterweightTorque, MeasuringConRodJournals,
                     MeasuringMainJournals, MinMaxValue, ImageCrankshaft)


class EngineNumberWidger(s2forms.ModelSelect2Widget):
    search_fields = [
        'engine_number__icontains',
    ]


class VisualCheckConRodJournalsForm(forms.ModelForm):
    class Meta:
        model = VisualCheckConRodJournals

        fields = ['engine_number',
                  'con_journal_1',
                  'con_journal_2',
                  'con_journal_3',
                  'con_journal_4',
                  'con_journal_5',
                  'con_journal_6',
                  'con_journal_7',
                  'con_journal_8',
                  'con_journal_9',
                  'con_journal_10'
                  ]
        widgets = {
            'engine_number': EngineNumberWidger,
        }


class VisualCheckMainJournalsForm(forms.ModelForm):
    class Meta:
        model = VisualCheckMainJournals

        fields = ['main_journal_1',
                  'main_journal_2',
                  'main_journal_3',
                  'main_journal_4',
                  'main_journal_5',
                  'main_journal_6',
                  'main_journal_7',
                  'main_journal_8',
                  'main_journal_9',
                  'main_journal_10',
                  'main_journal_11'
                  ]


class CheckСounterweightTorqueForm(forms.ModelForm):
    class Meta:
        model = CheckСounterweightTorque

        fields = ['torque',
                  'counterweight_1',
                  'counterweight_2',
                  'counterweight_3',
                  'counterweight_4',
                  'counterweight_5',
                  'counterweight_6',
                  'counterweight_7',
                  'counterweight_8',
                  'counterweight_9',
                  'counterweight_10',
                  'counterweight_11',
                  ]


class MeasuringConRodJournalsForm(forms.ModelForm):
    class Meta:
        model = MeasuringConRodJournals

        fields = ['con_journal_1_meas',
                  'con_journal_2_meas',
                  'con_journal_3_meas',
                  'con_journal_4_meas',
                  'con_journal_5_meas',
                  'con_journal_6_meas',
                  'con_journal_7_meas',
                  'con_journal_8_meas',
                  'con_journal_9_meas',
                  'con_journal_10_meas'
                  ]


class MeasuringMainJournalsForm(forms.ModelForm):
    class Meta:
        model = MeasuringMainJournals

        fields = ['main_journal_1_meas',
                  'main_journal_2_meas',
                  'main_journal_3_meas',
                  'main_journal_4_meas',
                  'main_journal_5_meas',
                  'main_journal_6_meas',
                  'main_journal_7_meas',
                  'main_journal_8_meas',
                  'main_journal_9_meas',
                  'main_journal_10_meas',
                  'main_journal_11_meas'
                  ]


class MinMaxValueForm(forms.ModelForm):
    class Meta:
        model = MinMaxValue

        fields = ['min_val',
                  'max_val',
                  'unit',
                  'measuring_tool'
                  ]


class ImageCrankshaftForm(forms.ModelForm):
    class Meta:
        model = ImageCrankshaft
        fields = ['image',]
        

    image = MultiImageField(label=u'Фотографии дефектов')


class SingleImageForm(forms.ModelForm):
    class Meta:
        model = ImageCrankshaft
        fields = ['image',]
