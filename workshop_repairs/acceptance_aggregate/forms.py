from django import forms
from django_select2 import forms as s2forms
from multiupload.fields import MultiImageField

from .models import AcceptanceAggregate, Image


class EngineNumberWidger(s2forms.ModelSelect2Widget):
    search_fields = [
        'engine_number__icontains',
    ]


class AcceptanceAggregateForm(forms.ModelForm):
    class Meta:
        model = AcceptanceAggregate

        fields = ['engine_number',
                  'transport_frame',
                  'transport_frame_com',
                  'damper',
                  'damper_count',
                  'cylinder_head',
                  'cylinder_head_count',
                  'fuel_pump',
                  'fuel_pump_count',
                  'description',
                  ]
        widgets = {
            'engine_number': EngineNumberWidger,
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image',]
        

    image = MultiImageField(label=u'Фотографии')


class SingleImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image',]
