from django import forms


class MedicForm(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')
    surname = forms.CharField(max_length=20, label='Apellido')
    medic_type = forms.CharField(max_length=20, label='Especialidad')