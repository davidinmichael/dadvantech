from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="index"),
	path('solar-products', views.products_in_drive, name="products_in_drive"),
]
