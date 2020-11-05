from django.contrib import admin

# Register your models here.
from contacts.models import Contacts, Names

admin.site.register(Contacts)
admin.site.register(Names)
