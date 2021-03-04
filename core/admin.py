from django.contrib import admin

from core.models import Product,Size,Order,OrderItem

admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(OrderItem)