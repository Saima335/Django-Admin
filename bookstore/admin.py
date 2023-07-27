from django import forms
from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

from . import models
from .models import Profile, Customer

# Register your models here.
class BookstoreAdminArea(admin.AdminSite):
    site_header = "Bookstore Admin Area"

bookstore_site = BookstoreAdminArea(name="BookstoreAdmin")

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'Wrong csv file')
                return HttpResponseRedirect(request.path_info)
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            for x in csv_data:
                fields = x.split(",")
                if len(fields) == 2:
                    print(fields)
                    Customer.objects.update_or_create(name = fields[0], balance = fields[1])
            url = reverse('admin:index')
            return HttpResponseRedirect(url)
        form = CsvImportForm()
        data = {'form':form}
        return render(request, 'admin/csv_upload.html', data)

admin.site.register(Customer, CustomerAdmin)

# class TestAdminPermissions(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return True
#     def has_change_permission(self, request, obj=None):
#         return obj is None or obj.title!="abc"
#     def has_delete_permission(self, request, obj=None):
#         if obj != None and request.POST.get('action') == 'delete_selected':
#             messages.add_message(request, messages.ERROR,(
#                 'I really hope you want to delete this movie'
#             ))
#         # if request.user.groups.filter(name="editors").exists():
#         #     return False
#         return True
#     def has_view_permission(self, request, obj=None):
#         return obj

# bookstore_site.register(models.Movie, TestAdminPermissions)
# bookstore_site.register(models.Book)
# bookstore_site.register(models.Customer)

# class EmailFilter(SimpleListFilter):
#     title = 'Email Filter'
#     parameter_name = 'user_email'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('has_email', 'has_email'),
#             ("no_email", "no_email")
#         )
#     def queryset(self, request, queryset):
#         if not self.value():
#             return queryset
#         if self.value().lower() == 'has_email':
#             return queryset.exclude(user__email='')
#         if self.value().lower() == 'no_email':
#             return queryset.filter(user__email='')
#
# class Filter(admin.ModelAdmin):
#     list_display = ("id", "email", "created_at", "role", "is_active")
#     list_filter = ("is_active", "role", "created_at", EmailFilter)
#
# admin.site.register(Profile, Filter)


