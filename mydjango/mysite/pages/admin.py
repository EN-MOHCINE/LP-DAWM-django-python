# Register your models here.
from django.contrib import admin
from .models import  Page 


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'permalink', 'updated_at')
    ordering = ('title',)
    search_fields = ('title',)
admin.site.register(Page ,PageAdmin)