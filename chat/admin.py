from dataclasses import fields
from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    fields = ("chat", "text", "author", "receiver", "created_at")
    list_display = ("text", "author", "receiver", "created_at")
    search_fields = ("text",)


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
