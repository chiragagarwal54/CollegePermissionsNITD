from . import views
from django.urls import path

urlpatterns = [
  path('<slug:username>/<slug:building>/<slug:room>/permission/', views.permission, name='permission'),
  path('<slug:username>/<slug:building>/', views.RoomList, name='RoomList'),
  path('<slug:username>/submittedforms/', views.SubForm, name='SubForm'),
  path('<slug:username>/', views.Base, name='base'),
  path('login/', views.login_view, name='login'),
]
