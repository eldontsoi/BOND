from django.shortcuts import render

def index(request):
    return render(request, 'bond/index.html', {})

def room(request, room_name):
    return render(request, 'bond/room.html', {
        'room_name': room_name
    })