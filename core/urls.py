from django.urls import path
from .views import index, return_images_as_json

urlpatterns = [
    path("", index, name="index"),
    path("api/images/", return_images_as_json, name="images")
]
