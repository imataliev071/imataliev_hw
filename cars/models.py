from django.db import models


# Create your models here.
class Cars(models.Model):
    cars_name = models.CharField(max_length=100)
    cars_image = models.ImageField(upload_to='')
    cars_price = models.DecimalField(max_digits=10, decimal_places=2)
    cars_description = models.TextField()
    cars_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cars_name

