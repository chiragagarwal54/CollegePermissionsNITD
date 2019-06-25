from . import views
from django.urls import path

urlpatterns = [
  path('', views.base, name='base'),
  path('<int:building_id>', views.RoomList, name='RoomList'),
  path('login/', views.login_view, name='login'),
  path('permission/new', views.permission, name='permission'),
  path('subform', views.SubForm, name='SubForm'),
]
