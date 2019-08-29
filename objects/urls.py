from . import views
from django.urls import path

urlpatterns = [
  path('<int:building_id>/<slug:room>/permission/', views.permission, name='permission'),
  path('<int:building_id>/permission/new/', views.permission, name='permission'),
  path('<int:building_id>/', views.RoomList, name='RoomList'),
  path('submittedforms/', views.SubForm, name='SubForm'),
  path('', views.Base, name='base'),
  path('login/', views.login_view, name='login'),
]
