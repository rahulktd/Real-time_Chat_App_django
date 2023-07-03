from django.shortcuts import render

from chat_room.models import ChatRoom, Message


# Create your views here.

def chat_room(request):
    rooms = ChatRoom.objects.all()
    return render(request,'rooms.html',{'rooms':rooms})

def room(request,slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request,'chat_room.html',{'room':room,'messages': messages})