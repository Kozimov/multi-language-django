from modeltranslation.translator import register, TranslationOptions
from .models import Info

@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)