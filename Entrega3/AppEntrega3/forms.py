from django import forms

class DestinoFormulario(forms.Form):
    pais = forms.CharField(max_length=30)
    ciudad = forms.CharField(max_length=30)

class HospedajeFormulario(forms.Form):
    Tipo_Hospedaje= forms.CharField(max_length=30)
    Zona= forms.CharField(max_length=30)
    Cantidad_Personas= forms.IntegerField()
    
class Alquiler_CochesFormulario(forms.Form):
    Alta_Gama= forms.CharField(max_length=30)
    Media_Gama= forms.CharField(max_length=30)
    Compacto= forms.CharField(max_length=30)
    

       