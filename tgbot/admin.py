from django.contrib import admin
from .models import TgUser
class TgUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 
        'chat_id',
        'created'
        )
admin.site.register(TgUser, TgUserAdmin)