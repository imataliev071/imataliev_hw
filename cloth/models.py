from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=10)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('На обработке', 'На обработке'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
