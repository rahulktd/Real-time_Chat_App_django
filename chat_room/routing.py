from django.urls import path

from chat_room import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/',consumers.ChatConsumer.as_asgi()),
]