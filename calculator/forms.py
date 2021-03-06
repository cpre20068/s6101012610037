from django import forms
from .models import Calc
class CalcForm(forms.ModelForm):
    operation_type = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/'),
    ]
    operations = forms.CharField(label="Choose operation", widget=forms.Select(choices=operation_type))
    class Meta:
        model = Calc
        fields = ('x','y','operations',)