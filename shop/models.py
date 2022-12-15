from django.db import models

# Create your models here.
class Firm(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    firm = models.ForeignKey(Firm,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
