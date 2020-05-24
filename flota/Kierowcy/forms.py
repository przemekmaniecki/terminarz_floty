from django import forms
from Kierowcy.models import *

class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Kierowcy
        fields = '__all__'

class BridgeForm(forms.Form):
    id = forms.IntegerField(required=True, label="")

class AddPjForm(forms.ModelForm):
    class Meta:
        model = PrawoJazdy
        exclude = ['kierowca']

class AddKwForm(forms.ModelForm):
    class Meta:
        model = Kwalifikacja
        exclude = ['kierowca']

class AddAdrForm(forms.ModelForm):
    class Meta:
        model = ADRdriver
        exclude = ['kierowca']

