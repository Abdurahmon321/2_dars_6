from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, ShippingAddress, Review
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "is_active", "created_at")
    list_display_links = ("name",)
    search_fields = ("id", "name")
    list_filter = ("id", "name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description")
    search_fields = ("id", "name")
    list_display_links = ("name",)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("id", "name")
    list_display_links = ("name",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "date_ordered", "customer")
    search_fields = ("id", "name")
    list_display_links = ("id",)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity", "order", "product")
    search_fields = ("id", "order")
    list_display_links = ("quantity",)


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "customer", "order")
    search_fields = ("id", "customer")
    list_display_links = ("address",)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "comment", "customer", "product")
    search_fields = ("id", "customer", "product")
    list_display_links = ("id",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Review, ReviewAdmin)
