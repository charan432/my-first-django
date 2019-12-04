from django.contrib import admin

# to Hide 'Groups' section from the admin panel
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact

# To use import/export feature in admin panel
from import_export.admin import ImportExportModelAdmin

# Customise Contact page in Admin panel. Pass className (ContactAdmin as a 2nd argument in site.reigster for 'Contact')


class ContactAdmin(ImportExportModelAdmin):
    # To show these details in a table in admin page
    list_display = ('id', 'name', 'email', 'gender', 'info',
                    'phone', 'date_added', 'image')
    # Show links for these fields in admin panel
    list_display_links = ('id', 'name')

    list_per_page = 10  # set pagination limit for each page
    # Search params in the admin page
    search_fields = ('name', 'email', 'phone', 'email')
    list_filter = ('gender',)


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)  # to Hide 'Groups' section from the admin panel
