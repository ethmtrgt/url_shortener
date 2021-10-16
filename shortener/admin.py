from django.contrib import admin
from .models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display=["alias","long_url","visits","creation_date"]
    ordering=["-visits"]
