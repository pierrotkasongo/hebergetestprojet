from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='images', blank=True,default='aucune image')
    name = models.CharField(max_length=50, default='aucune nom')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name