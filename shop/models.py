from django.db import models
from django.utils import timezone

class Product(models.Model):
	name = models.TextField(max_length=30)
	price = models.PositiveIntegerField()
	discount = models.IntegerField()
	rating = models.FloatField()
	stock = models.IntegerField()
	is_avaliable = models.BooleanField()
	desc = models.TextField()
	img = models.ImageField(upload_to="img/", blank= True)
	likes = models.IntegerField(default=0)

def __str__(self):
	return self.name

class Order(models.Model):
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
	delivery_adress = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)



# Create your models here.
