from django.contrib import admin
from . import models
import django.apps
from django import forms
from .models import post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name="BlogaAdmin")

# admin.site.register(models.post)
# blog_site.register(models.post)

# TEXT = 'Some text that we include'
# @admin.register(post)
# class PostAdmin(admin.ModelAdmin):
#     # fields = ['title', 'author']
#     # fields = ['title', ('author', 'price')]
#     fieldsets = (
#         ('Section 1', {
#             'fields': ('title', 'author',),
#             'description': '%s' % TEXT,
#             'classes': ('wide',),
#         }),
#         ('Section 2', {
#             'fields': ('price',),
#             'classes': ('collapse',),
#         })
#     )
# admin.site.register(post, PostAdmin)

models = django.apps.apps.get_models()
print(models)

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
# admin.site.unregister(django.contrib.contenttypes.models.ContentType)
# admin.site.unregister(django.contrib.admin.models.LogEntry)
# admin.site.unregister(django.contrib.auth.models.Permission)
# admin.site.unregister(django.contrib.sessions.models.Session)


# class PostForm(forms.ModelForm):
#     def __int__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].help_text = 'Some Help Text'
#
#     class Meta:
#         model = post
#         exclude = ('author',)

# class PostAdminForm(admin.ModelAdmin):
#     form = PostForm
# admin.site.register(post, PostAdminForm)

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "author"

admin.site.register(post, SummerAdmin)
blog_site.register(post, SummerAdmin)