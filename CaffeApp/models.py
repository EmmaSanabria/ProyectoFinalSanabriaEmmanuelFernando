from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=240)
    price = models.IntegerField()
    available_choices = ( 
        ('avaible', 'Disponoble'),
        ('not avaible', 'No disponible')
    )
    available = models.CharField(max_length=15, choices= available_choices )
    veggie_option = models.CharField(max_length=15, choices= available_choices )
    image = models.ImageField(upload_to='product/', null=True, blank=True, default='image')
    
    def _str_(self):
        return f'{self.name} --> {self.price}'
    
class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_guests = models.IntegerField()
    date = models.DateField()
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
    time = models.CharField(max_length=15, choices= time_choices )
    message = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.name
        
class Staff(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    job = models.CharField(max_length=40)
    workshift_choices = ( 
        ('morning', 'Mañana'),
        ('evening', 'Tarde'),
    )
    workshift = models.CharField(max_length=15, choices= workshift_choices )
    age = models.IntegerField()
    image = models.ImageField(upload_to='staff/', null=True, blank=True, default='image')
    
    def __str__(self):
        return f" {self.name} -- {self.last_name}"
    
class Promo_menu(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=240)
    price = models.IntegerField()
    choices = ( 
        ('avaible', 'Disponoble'),
        ('not avaible', 'No disponible')
    )
    available = models.CharField(max_length=15, choices= choices )
    veggie_option = models.CharField(max_length=15, choices= choices )
    image = models.ImageField(upload_to='promo/', null=True, blank=True, default='image')
    
    def _str_(self):
        return f'{self.name} --> {self.price}'

