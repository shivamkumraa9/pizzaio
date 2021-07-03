from django.contrib import admin

from core.models import (Product, Size, Order, OrderItem)

admin.site.register([Product, Size])

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['name', 'price', 'quantity', 'size_name']
    readonly_fields = ('name', 'price', 'quantity', 'size_name')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ('name', 'email', 'phone', 'country', 'city', 
        'address_1', 'address_2', 'order_id', 'total', 'tax')

    inlines = [
        OrderItemInline,
    ]


admin.site.register(Order, OrderAdmin)
