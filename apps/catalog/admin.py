
from django.contrib import admin
from apps.catalog.models import Category,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}