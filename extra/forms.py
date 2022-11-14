from django.forms import DateInput, ModelForm
from extra.models import Turns

# class TurnsForm(forms.Form):
#     day = forms.DateField(label='Fecha del Turno', widget=forms.DateInput(attrs={'placeholder': 'mm-dd-yyyy'}))

class TurnsForm(ModelForm):
    class Meta:
        model = Turns
        fields = ['day']
        widgets = {
            'day': DateInput(attrs={'type':'date'}),
        }
        labels = {
            'day' : 'Dia del turno'
        }