from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.name}'
    
class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description= models.TextField(max_length=240)
    price = models.IntegerField()
    image = models.ImageField(null= True, blank= True, default= 'image')

    def __str__(self):
        return f'{self.name} --> {self.price}'
    
class Reservation(models.Model):
    name = models.CharField(max_length=50, unique=True)
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
        
