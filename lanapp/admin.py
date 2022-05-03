from django.contrib import admin
from .models import Info

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

