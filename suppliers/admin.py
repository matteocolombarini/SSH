from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'is_blacklisted']
    list_filter = ['is_blacklisted']
    search_fields = ['company_name', 'user__username']