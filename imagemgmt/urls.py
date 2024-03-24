from django.urls import path
from .views import RemoveBGImage

urlpatterns = [
    path("remove", RemoveBGImage.as_view(), name="remove_bg"),
]
