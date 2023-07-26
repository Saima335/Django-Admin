from django.contrib import admin
from . import models

# Register your models here.
class BookstoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Admin Area"

bookstore_site = BookstoreAdminArea(name="BookstoreAdmin")