from django.contrib import admin
from .models import *
# Register your models here.
class depAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(department,depAdmin)

class docAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(doctor,docAdmin)

admin.site.register(patient)