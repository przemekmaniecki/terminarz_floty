from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import PojazdyModel, BT, tacho, ADR, NormaCzystosciSpalin, FRC, UDT, TDT, UKO


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = PojazdyModel
        fields = ('rodzaj', 'marka', 'model', 'VIN', 'nr_rej', 'rok_prod')

class BT_Form(forms.ModelForm):
    class Meta:
        model = BT
        fields = ['instytucja', 'wymagane', 'data_konc']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instytucja'].widget.attrs.update(size='50')
        self.fields['data_konc'].required = False
        self.fields['wymagane'].required = False

class TACHO_Form(forms.ModelForm):
    class Meta:
        model = tacho
        fields = ['instytucja', 'wymagane', 'data_konc']

class ADR_Form(forms.ModelForm):
    class Meta:
        model = ADR
        fields = ['instytucja', 'wymagane', 'data_konc']

class EURO_Form(forms.ModelForm):
    class Meta:
        model = NormaCzystosciSpalin
        fields = ['wymagane', 'norma']

class FRC_Form(forms.ModelForm):
    class Meta:
        model = FRC
        fields = ['instytucja', 'wymagane', 'data_konc']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instytucja'].widget.attrs.update(size='40')
        self.fields['instytucja'].required = False
        self.fields['data_konc'].required = False
        self.fields['wymagane'].required = False
class UDT_Form(forms.ModelForm):
    class Meta:
        model = UDT
        fields = ['instytucja', 'wymagane', 'data_konc']

class TDT_Form(forms.ModelForm):
    class Meta:
        model = TDT
        fields = ['instytucja', 'wymagane', 'data_konc']
class UK_Form(forms.ModelForm):
    class Meta:
        model = UKO
        fields =[
            'instytucja', 'data_konc', 'nr_polisy',
            'OC', 'AC', 'NNW'
            ]

class SearchForm(forms.Form):
    text = forms.CharField(max_length=40, required=False, label="")

class BridgeForm(forms.Form):
    nr = forms.IntegerField(required=True, label="")



class BridgeDateForm(forms.Form):
    date2 = forms.CharField(max_length=10, required=True, label="", help_text="yyyy-mm-dd")

