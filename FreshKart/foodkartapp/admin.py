from django.contrib import admin
from .models import *

# Register your models here.

class categ(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categ)

class prodadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,prodadmin)

admin.site.register(cartlist)
admin.site.register(items)