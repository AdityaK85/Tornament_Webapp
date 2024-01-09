from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create_room(request):
    return render(request, 'create_room.html')