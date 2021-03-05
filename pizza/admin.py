from django.contrib import admin
# import the models 
from .models import Pizza, Size

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['topping1', 'topping2']



# Register your models here.
admin.site.register(Pizza)
admin.site.register(Size)