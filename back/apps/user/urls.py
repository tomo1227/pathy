from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ActivateUser

urlpatterns = [
    path(
        "users/activation/<uid>/<token>",
        ActivateUser.as_view({"get": "activation"}),
        name="activation",
    ),
]
