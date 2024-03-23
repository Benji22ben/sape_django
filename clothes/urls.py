from django.urls import path
from .views import UserClothing, AppClothing, CreateCoherentOutfit

urlpatterns = [
    path("user", UserClothing.as_view(), name="user"),
    path("", AppClothing.as_view(), name="app_clothes"),
    path(
        "create_outfit",
        CreateCoherentOutfit.as_view(),
        name="create_coherent_outfit",
    ),
]
