from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product

admin.site.register(Category)


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="60" height="60"')

    get_image.short_description = "Photo"


admin.site.site_title = 'ShopPrototype'
admin.site.site_header = 'ShopPrototype'
