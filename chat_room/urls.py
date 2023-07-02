from django.urls import path

from chat_room import views

urlpatterns = [
    path('chat_room',views.chat_room,name='chat_room'),
    path('room/<slug:slug>/',views.room,name='room'),
]