from django.db import models

# Create your models here.
    

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('CR', ('Cereals')),
        ('VE', ('Vegetables')),
        ('FD', ('Food')),
        ('FR', ('Fruits')),
        ('OT', ('Other')),
    ]
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='Products')
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='OT', 
        verbose_name=("Product Category") 
    )

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    