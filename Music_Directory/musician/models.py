from django.db import models
# Create your models here.

class Musician(models.Model):
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_no = models.CharField(max_length = 13)
    CHOICES = [('Percussion','Percussion'),('Guitar','Guitar'),('Woodwind','Woodwind'),('Keyboard','Keyboard')]
    instrument_type = models.CharField(choices = CHOICES,max_length= 50)
    
    def __str__(self):
        return f'Name: {self.f_name} {self.l_name}'