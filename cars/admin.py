from django.contrib import admin
from .models import Brand, Car

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'factory_year', 'model_year', 'color', 'owner', 'description', 'created_at', 'updated_at')
    search_fields = ('model',)
    list_filter = ('brand',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)