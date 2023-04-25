from django import forms
from django.forms import DateInput
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class MessagesForm(forms.Form):
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
        fields = ['name', 'description', 'price', 'available', 'veggie_option', 'image']
        
class EditUserForm(UserChangeForm):
    password= forms.CharField(
        help_text="",
        widget=forms.HiddenInput() , required=False     
    )
    
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields= ('email', 'first_name', 'last_name', 'password1', 'password2')
        
    def clean_password(self):
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("las contraseñas no coinciden!")
        return password2
    
class StaffForm(forms.Form):
    class Meta:
        model = Staff
        fields= ('name','last_name', 'job', 'workshift', 'age', 'image')
        
class AddPromoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'veggie_option', 'image']