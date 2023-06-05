from django.contrib import admin
from .models import ChatUser, ChatMessage


@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    pass
