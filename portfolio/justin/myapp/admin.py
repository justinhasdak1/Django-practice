from django.contrib import admin
from .models import Contact

@admin.register(Contact)  # ✅ Recommended when you need customization
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Display specific columns
    search_fields = ('name', 'email')  # Add search functionality
