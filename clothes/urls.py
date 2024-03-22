from django.urls import path
from .views import UserClothing, AppClothing

urlpatterns = [
    path("user/", UserClothing.as_view(), name="user"),
    path("", AppClothing.as_view(), name="app_clothes"),
]
