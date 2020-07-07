from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
	user 	= models.OneToOneField(User, on_delete=models.CASCADE)
	name	= models.CharField(max_length=200)
	email 	= models.EmailField()

	def __str__(self):
		return self.name

class Product(models.Model):
	name	= models.CharField(max_length=100)
	price	= models.FloatField()
	digital = models.BooleanField(default=False)
	images  = models.ImageField(default='default.jpg')

	def __str__(self):
		return self.name

class Order(models.Model):
	customer 		= models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	date_ordered	= models.DateTimeField(auto_now_add=True)
	complete 		= models.BooleanField(default=False)
	transaction_id	= models.CharField(max_length=100)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		myorder = self.orderitem_set.all()
		total = sum([item.get_total for item in myorder])
		return total


	@property
	def get_cart_items(self):
		myorder = self.orderitem_set.all()
		total = sum([item.quantity for item in myorder])
		return total
	
	

class OrderItem(models.Model):
	product 	= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order     	= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity 	= models.IntegerField(default=0)
	date_added  = models.DateTimeField(auto_now_add=True)	

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order 	 = models.ForeignKey(Order, on_delete=models.CASCADE)
	address  = models.CharField(max_length=200)
	city	 = models.CharField(max_length=200)
	state 	 = models.CharField(max_length=200)
	zipcode  = models.CharField(max_length=6)
	date_added  = models.DateTimeField(auto_now_add=True)

	def	__str__(self):
		return self.address

