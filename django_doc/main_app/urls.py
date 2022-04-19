from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('things/', views.ThingList.as_view(), name='things_index'),
    path('things/create', views.ThingCreate.as_view(), name='things_create'),
]