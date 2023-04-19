from django import forms
from django.forms import DateInput
from .models import *

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    number_guests = forms.IntegerField()
    date =  forms.DateField(label='Fecha de reserva' ,
                            widget=DateInput(attrs={'type': 'date'}))
    
    time_choices =  (
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
    )
    time = forms.ChoiceField(choices= time_choices)
    message = forms.CharField(widget=forms.Textarea)
    
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']