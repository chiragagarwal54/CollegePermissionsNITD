from . import views
from django.urls import path

urlpatterns = [
  path('', views.base, name='base'),
  path('<int:building_id>', views.RoomList, name='RoomList'),
]
