from django.contrib import admin
from .models import Info
from modeltranslation.admin import TranslationAdmin

@admin.register(Info)
class InfoAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}

