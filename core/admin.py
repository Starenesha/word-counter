from django.contrib import admin

# Register your models here.
from .models import Text

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass