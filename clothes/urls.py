from django.urls import path
from .views import UserClothingListView

urlpatterns = [
    path("user/", UserClothingListView.as_view(), name="user"),
]
