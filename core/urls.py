from django.urls import path
from . import views
from .views import JoinCommunityView


urlpatterns = [
	path('', views.index, name="index"),
	path('solar-products/', views.products_in_drive, name="products_in_drive"),
	path('solar-generators/', views.solar_products, name="solar_generator"),
	path('solar-generator/<int:pk>/', views.solar_product,
	     name="solar_generator_details"),
    path("join-community/", JoinCommunityView.as_view(), name="join_community")
]
