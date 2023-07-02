from django.shortcuts import render

from chat_room.models import ChatRoom


# Create your views here.

def chat_room(request):
    rooms = ChatRoom.objects.all()
    return render(request,'rooms.html',{'rooms':rooms})

def room(request,slug):
    room = ChatRoom.objects.get(slug=slug)
    return render(request,'chat_room.html',{'room':room})