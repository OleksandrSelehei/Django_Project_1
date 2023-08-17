from django.contrib import admin
from .models import Orders, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('user_name', 'user_surname', 'email', 'state')
    search_fields = ('user_name', 'user_surname', 'email')


admin.site.register(Orders, OrderAdmin)
admin.site.register(OrderItem)
