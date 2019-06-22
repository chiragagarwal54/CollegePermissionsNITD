from django.shortcuts import render, get_object_or_404
from objects.models import Building, Room
from django.views import generic

def base(request):
    buildings = Building.objects.all()
    #rooms = room.objects.filter('centre')
    return render(request, 'base.html', {'buildings': buildings})

def RoomList(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    return render(request, 'roomlist.html', context={'building': building})

#class RoomList(generic.ListView):
#    model = Building
    #return render(request, 'building_list.html', context={'building':building})
