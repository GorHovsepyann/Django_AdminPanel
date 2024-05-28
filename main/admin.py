from django.contrib import admin
from .models import category,subcategory
from unfold.admin import ModelAdmin
# Register your models here.

    
    
@admin.register(category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(subcategory)
class SubcategoryAdmin(ModelAdmin):
    pass
# admin.site.register(category)
# admin.site.register(subcategory)

