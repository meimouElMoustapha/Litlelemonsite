from django.db import models

# Create your models here.


class Menu(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='images',default='images/images_2.png')

    def __str__(self):
        return self.Name
    
class Book(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    phone_number = models.CharField(blank=True, help_text='Contact phone number',max_length=100)

    image=models.ImageField(upload_to='images',default='images/images_2.png')

    def __str__(self):
        return self.Name
