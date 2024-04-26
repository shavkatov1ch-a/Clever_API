from django.contrib import admin
from .models import Contact, ContactInfo



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('created_at', 'updated_at')


admin.site.register(ContactInfo)