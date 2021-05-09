from django.urls import path
from . import views

urlpatterns = [
	path('', views.itemList, name='home'),
	path('itemNew', views.itemNew, name='itemNew'),
	path('itemChange/<int:pk>/', views.itemChange, name='itemChange'),
]
