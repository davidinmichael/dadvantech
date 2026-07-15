from django.urls import path
from . import views
from .views import JoinCommunityView


urlpatterns = [
    path("", views.index, name="index"),
    path("solar-products/", views.products_in_drive, name="products_in_drive"),
    path("solar-generators/", views.solar_products, name="solar_generator"),
    path(
        "solar-generator/<int:pk>/", views.solar_product, name="solar_generator_details"
    ),
    path("join-community/", JoinCommunityView.as_view(), name="join_community"),
    path("digital-literacy/", views.digital_literacy, name="digital_literacy"),
    path("digital-products/", views.digital_products, name="digital_products"),
    path(
        "digital-skills-remote-jobs/",
        views.digital_skills_and_remote_jobs,
        name="digital_skills_and_remote_jobs",
    ),
    path("camp/", views.summer_code, name="summer_code"),
]
