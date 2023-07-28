from django.contrib import admin

from base.models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
