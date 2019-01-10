from django.contrib import admin

# Register your models here.

from .models import Design, Message

class DesignAdmin(admin.ModelAdmin):
    list_display = ['name', 'design_type', 'caption', 'timestamp',]


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'sender_email', 'subject', 'timestamp']


admin.site.register(Design, DesignAdmin)
admin.site.register(Message, MessageAdmin)