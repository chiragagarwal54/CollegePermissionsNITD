from django.shortcuts import render
from objects.models import building, room

def base(request):
    buildings = building.objects.all()
    rooms = room.objects.select_related('centre')
    return render(request, 'base.html', {'buildings': buildings, 'rooms': rooms})
