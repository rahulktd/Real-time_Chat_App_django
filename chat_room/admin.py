from django.contrib import admin

from chat_room.models import ChatRoom,Message

# Register your models here.
admin.site.register(ChatRoom),
admin.site.register(Message),
