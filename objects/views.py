from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from objects.models import Building, Room, Permissionform
from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .form import *
from django.template import RequestContext
from .decorators import student_required
from django.contrib.auth.decorators import login_required


def base(request):
    buildings = Building.objects.all()
    forms = Permissionform.objects.all()
    #rooms = room.objects.filter('centre')
    return render(request, 'base.html', {'buildings': buildings},{'forms': forms})

def RoomList(request, building_id):
    building = get_object_or_404(Building, id=building_id)
    return render(request, 'roomlist.html', context={'building': building})


def login_view(request):
    _message = 'Log in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('base')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')


def permission(request):
    if request.method=="POST":
        form=PermForm(data=request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save()
            return redirect('base')
    else:
        form = PermForm()
    context = {'form': form}
    return render(request, 'requestform.html', context)

def SubForm(request):
    sub = Permissionform.objects.all()
    context = {'sub': sub}
    return render(request, 'subform.html', context)
