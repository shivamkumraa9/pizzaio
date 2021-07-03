from django.db import models

class Product(models.Model):
	catagory = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.CharField(max_length=100)
	sm_image = models.CharField(max_length=100)
	has_offer = models.BooleanField(default=False)
	price = models.FloatField(default=12.99)

	def __str__(self):
		return self.name

class Size(models.Model):
	name = models.CharField(max_length=10)
	price = models.FloatField()
	product = models.ManyToManyField(Product)

	def __str__(self):
		return self.name 


class Order(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	address_1 = models.CharField(max_length=100)
	address_2 = models.CharField(max_length=100, blank=True, null=True)
	order_id = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100, default='Processing')
	total = models.FloatField(blank=True, null=True)
	tax = models.FloatField(default=0, blank=True, null=True)

	def __str__(self):
		return self.name

class OrderItem(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()
	quantity = models.IntegerField()
	size_name = models.CharField(max_length=10)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
