from django.contrib import admin
from .models import Borders

# Register your models here.
class BorderAdmin(admin.ModelAdmin):
    #list_display: '__all__'
    list_display: ['name', 'price', 'date']
    



admin.site.register(Borders, BorderAdmin)
