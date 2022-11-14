from django import forms

class PacientForm(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')
    surname = forms.CharField(max_length=20, label='Apellido')
    dni = forms.IntegerField(label='Numero Documento')